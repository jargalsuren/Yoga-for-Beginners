from .models import * 

def get_all_users():
    """
        Getting all the users from the table. 
    """
    user = User.query.all()
    return user 

def get_all_videos():
    """
        Getting all the videos from the table.
    """
    video = Video.query.all()
    return video

def get_id_user(user_id):
    """
        Getting users according their id. 
    """
    user = User.query.get(user_id)
    return user
    
def get_username_user(username):
    """
		Getting users according to their username. 
    """
    user = User.query.filter_by(username=username)
    return user

def get_video_by_id(id):
    """
		Getting videos according to id. 
    """
    video = Video.query.get(id)
    return video

def get_type_video(video_type):
    """
		Getting videos according to the type.
    """ 
    video = Video.query.filter_by(video_type = video_type)
    return video

def get_name_video(name):
    """
        Getting videos according to their name.
    """
    video = Video.query.filter_by(name=name)
    return video

def get_all_videos_saved_by_user(user_id):
    """
        Getting all the videos favorited by a single user.
    """
    user_videos = SavedVideo.query.filter_by(user_id=user_id)
    return user_videos

# def get_all_courses():
#     """
#         Getting all the videos from the table.
#     """
#     courses = Courses.query.all()
#     return courses