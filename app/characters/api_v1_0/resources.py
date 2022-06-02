from flask import request, Blueprint
from flask_restful import Api, Resource

from app.common.error_handling import ObjectNotFound

from .schemas import CrewSchema
from ..models import Crew, Character, DevilFruit

crews_v1_0_bp = Blueprint('crews_v1_0_bp', __name__)

crew_schema = CrewSchema()

api = Api(crews_v1_0_bp)

class CrewListResource(Resource):

    def get(self):
        crews = Crew.get_all()
        result = crew_schema.dump(crews, many=True)
        return result

    def post(self):
        data = request.get_json()
        crew_dict = crew_schema.load(data)

        crew = Crew(name=crew_dict['name'], ship=crew_dict['ship'], status=crew_dict['status'], members=[])
        
        for member in crew_dict['members']:
            member_to_put = Character(member['name'], member['status'], member['origin'])
            member_to_put.devil_fruit_id = DevilFruit(member['devilfruit'])
            
            crew.members.append(member_to_put)

        crew.save()
        resp = crew_schema.dump(crew)
        return resp, 201

class CrewResource(Resource):
    def get(self, crew_id):
        crew = Crew.get_by_id(crew_id)
        if crew is None:
            raise ObjectNotFound('The Crew doesn\'t exist')
        resp = crew_schema.dump(crew)

        return resp

api.add_resource(CrewListResource, '/api/v1.0/crews/', endpoint='crews_list_resource')
api.add_resource(CrewResource, '/api/v1.0/crews/<int:crew_id>', endpoint='crews_resource')
