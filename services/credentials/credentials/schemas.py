from marshmallow import Schema, fields


class OrderDetailSchema(Schema):
    id = fields.Int(required=True)
    product_id = fields.Str(required=True)
    price = fields.Decimal(as_string=True)
    quantity = fields.Int()
    deneme = fields.Int(required=True)


class OrderSchema(Schema):
    id = fields.Int(required=True)
    deneme = fields.Int(required=True)
    order_details = fields.Nested(OrderDetailSchema, many=True)
