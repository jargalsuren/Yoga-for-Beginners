import unittest
from web.models import User, Video, User_Video
from web.queries import * 

#making some fake data to test the queries
class TestTheQueries(unittest.TestCase):
    def setUp(self):
        user_1 = User(user_id = 1, 
                      username = 'greatusername', 
                      user_password = 'whatanamazingpassword', 
                      user_level = '2')
        user_2 = User(user_id = 2, 
                      username = 'anotheruser', 
                      user_password = 'mehpassword', 
                      user_level = '1')
        
        video_1 = Video(id = 1,
                        name = "Best Yoga Video",
                        channel_name = "Morning Yerevan",
                        video_type = 2, 
                        length = 600, 
                        video_url = "https://www.youtube.com/watch?v=v7AYKMP6rOE")
        video_2 = Video(id = 2,
                        name = "Worst Yoga Video",
                        channel_name = "Evening SF",
                        video_type = 2, 
                        length = 1200, 
                        video_url = "https://www.youtube.com/watch?v=oBu-pQG6sTY")
        
        trans_1 = User_Video(transaction_id = 1, 
                             adding_date = '2017-09-05 09:45:28', 
                             id_user = 2,
                             id_video = 1)
        trans_2 = User_Video(transaction_id = 2, 
                             adding_date = '2020-19-03 07:13:42', 
                             id_user = 1, 
                             id_video =2)
        
    def test_get_username_user(self):
        user_1 = User.query.all()
        user_1_username = user_1.username
        self.assertTrue(get_username_user(user_1_username), user_1)
        

    def test_get_id_user(self):
        user_1 = User.query.all()
        user_1_id = user_1.user_id
        self.assertTrue(get_id_user(user_1_id), user_1)
        
    
    def test_get_id_video(self):
        video_1 = Video.query.all()
        video_1_id = video_1.id
        self.assertTrue(get_id_video(video_1_id), video_1)
    
    def test_get_type_video(self):
        video_1 = Video.query.all()
        video_1_type = video_1.video_type
        self.assertTrue(get_type_video(video_1_type), video_1)

if __name__ == "__main__":
    unittest.main()