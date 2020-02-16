#!/usr/bin/env python3

from flask import Flask, request
from flask_nameko import FlaskPooledClusterRpcProxy
from flask_restplus import Resource, Api, fields
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from auth import authorize, authorizations, save_token, delete_token
from errors import error
from dynaconf import settings

# Flask setup
app = Flask(__name__)
app.config.update(dict(NAMEKO_AMQP_URI=settings["rabbit_uri"],
                       NAMEKO_POOL_RECYCLE=settings["pool_recycle"]))

# Flask RESTplus setup
api = Api(app, version='1.0', title='Marketplace Microservices - IOVA',
          description='Amazon, Ebay, Etsy, Gumtree  Webservices',
          authorizations=authorizations)

# Flask Limiter setup
limiter = Limiter(app, key_func=get_remote_address)

ns_auth = api.namespace("auth", description="Auth API")
ns_api = api.namespace("api", description="Features API")
ns_credentials = api.namespace("credentials", description="Credentials API")

# Nameko setup
rpc = FlaskPooledClusterRpcProxy()
rpc.init_app(app)

# Set up models
login_model = api.model('Login', {
    'username': fields.String(required=True, description='User name'),
    'password': fields.String(required=True, description='User password')
})


@ns_api.route('/<service>/<method>')
class APIController(Resource):
    # @api.doc(params={'name': 'Name to say Hello'})
    @api.doc(security="bearer")
    @api.doc(responses={401: "Not Authorized", 403: "Forbidden", 429: "Too many requests", 200: "OK",
                        500: "Internal server error"})
    # @authorize
    def get(self, service, method):
        try:
            service = eval('rpc.' + str(service))
            result = getattr(service, method)(123)
            return {"result": result}
        except Exception as e:
            return {"error": error(500, "Internal server error: {}".format(e))}, 500

    # @authorize
    def post(self, service, method):
        try:

            service = eval('rpc.' + str(service))
            result = getattr(service, method)(123)
            return {"result": result}
        except Exception as e:
            return {"error": error(500, "Internal server error: {}".format(e))}, 500


""" Crdentials API Management"""


@ns_credentials.route('/<service>')
class CredentialsController(Resource):
    @api.doc(security="bearer")
    @api.doc(responses={401: "Not Authorized", 403: "Forbidden", 429: "Too many requests", 200: "OK",
                        500: "Internal server error"})
    @authorize
    def get(self, service):
        try:
            message = rpc.woocommerce
            message = getattr(message, service)(123)
            return {"result": message}
        except Exception as e:
            return {"error": error(500, "Internal server error: {}".format(e))}, 500

    @authorize
    def post(self, service):
        try:
            message = rpc.woocommerce
            message = getattr(message, service)(123)
            return {"result": message}
        except Exception as e:
            return {"error": error(500, "Internal server error: {}".format(e))}, 500


""" Auth API Management """


@ns_auth.route('/login')
class LoginController(Resource):
    decorators = [limiter.limit(settings["limit_login"])]

    @api.doc(responses={403: "Forbidden", 429: "Too many requests", 200: "OK", 500: "Internal server error"})
    @api.expect(login_model)
    def post(self):
        try:
            payload = request.json
            res = rpc.auth_service.login(payload["username"], payload["password"])
            if "access_token" in res.keys():
                save_token(res["access_token"], settings["token_expiration"])
                return {"status": "Success",
                        "access_token": res["access_token"]}
            else:
                raise Exception("Unknown response format")
        except Exception as e:
            return {"status": "Unable to login",
                    "error": error(403, "Forbidden: {}".format(e))}, 403

    @api.doc(security="bearer")
    @api.doc(responses={429: "Too many requests", 200: "OK", 500: "Internal server error"})
    @limiter.limit(settings["limit_login"])
    @authorize
    def delete(self):
        try:
            delete_token()
            return {"status": "Success"}
        except Exception as e:
            return {"status": "Unable to logout",
                    "error": error(500, "Internal server error: {}".format(e))}, 500


@ns_auth.route('/register')
class RegisterController(Resource):
    decorators = [limiter.limit(settings["limit_api"])]

    @api.doc(security="bearer")
    @api.doc(responses={401: "Not Authorized", 403: "Forbidden", 429: "Too many requests", 200: "OK",
                        500: "Internal server error"})
    @authorize
    def post(self):
        try:
            message = rpc.greetings_service.hello("dsadas")
            return {"message": message}
        except Exception as e:
            return {"error": error(500, "Internal server error: {}".format(e))}, 500
