from flask import request
from flask_restx import Api, Resource, fields, reqparse
from flask_restx.namespace import Namespace
from models import Customer
from utils.http import unprocessable_entity

api = Api(
    version="1.0",
    title="Customer API",
    description="A back-end coding challenge by Zachary Mauldin for HEB",
    doc="/swagger",
    contact_email="zmsoftwareengineer@gmail.com",
    default="Customer",
    default_label="Customers endpoints",
)

resource_fields = api.model(
    "Customers",
    {
        "first_name": fields.String(required=True),
        "last_name": fields.String(required=True),
        "email": fields.String(required=True),
        "address": fields.String(required=True),
        "city": fields.String(required=True),
        "state": fields.String(required=True),
        "zipcode": fields.String(required=True),
    },
)


@api.route("/customers", endpoint="customers")
class CustomersView(Resource):
    """Customer"""

    parser = reqparse.RequestParser()
    parser.add_argument("city")

    @api.doc(params={"city": "The city of the customers"})
    def get(self):
        """Get all customers or filter by city"""
        args = self.parser.parse_args()
        city = args.get("city")

        if city:
            customers = Customer.get_by_city(city)
        else:
            customers = Customer.get_all()

        if customers is None:
            return unprocessable_entity()

        customers_json = [customer.get_json() for customer in customers]
        return customers_json

    @api.expect(resource_fields)
    def post(self):
        """Add a new customer"""
        customer_data = request.json
        Customer.create_customer(customer_data)
        customers = Customer.get_all()

        if customers is None:
            return unprocessable_entity()

        try:
            return customers[-1].get_json()
        except:
            return {}


@api.route("/customers/<int:customerId>")
class CustomerView(Resource):
    def get(self, customerId):
        """Get a specific customer by id"""
        customer = Customer.get_by_id(customerId)
        if customer is not None:
            return customer.get_json()
        return unprocessable_entity()
