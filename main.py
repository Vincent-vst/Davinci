from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	task = db.Column(db.String(100), nullable=False)
	pwd = db.Column(db.Integer, nullable=False)
	status = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f"Video(task = {task}, pwd = {pwd}, status = {status})"

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("task", type=str, help="task is required", required=True)
video_put_args.add_argument("pwd", type=int, help="pwd", required=True)
video_put_args.add_argument("status", type=int, help="status", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("task", type=str, help="task is required")
video_update_args.add_argument("pwd", type=int, help="pwd")
video_update_args.add_argument("status", type=int, help="status")

resource_fields = {
	'id': fields.Integer,
	'task': fields.String,
	'pwd': fields.Integer,
	'status': fields.Integer
}

class Video(Resource):
	@marshal_with(resource_fields)
	def get(self, video_id):
		result = VideoModel.query.filter_by(id=video_id).first()
		if not result:
			abort(404, message="Could not find task with that id")
		return result

	@marshal_with(resource_fields)
	def put(self, video_id):
		args = video_put_args.parse_args()
		result = VideoModel.query.filter_by(id=video_id).first()
		if result:
			abort(409, message="task is taken")

		video = VideoModel(id=video_id, task=args['task'], pwd=args['pwd'], status=args['status'])
		db.session.add(video)
		db.session.commit()
		return video, 201

	@marshal_with(resource_fields)
	def patch(self, video_id):
		args = video_update_args.parse_args()
		result = VideoModel.query.filter_by(id=video_id).first()
		if not result:
			abort(404, message="task doesn't exist, cannot update")

		if args['task']:
			result.task = args['task']
		if args['pwd']:
			result.pwd = args['pwd']
		if args['status']:
			result.status = args['status']

		db.session.commit()

		return result


	def delete(self, video_id):
		abort_if_video_id_doesnt_exist(video_id)
		del videos[video_id]
		return '', 204


api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
	app.run(debug=True, port=3002)
