import unittest
from web import app, db
from web.models import User, Videos

class BaseTestCase(unittest.TestCase):
  """
  A base test case
  """
  def create_app(self):
    app.config.from_object('config.TestConfig')
    return app
  
  def set_up(self):
    db.create_all()
    db.session.add(User(1,'somebodycool', 'goodstudent@uni.minerva.edu', 'verylongpassword'))
    db.session.add(Videos(1, "Flex & Stretch","FitOn", 15, "zwoVcrdmLOE", "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=3620&q=80"))
    db.session.commit()
    
  def tearDown(self):
    db.session.remove()
    db.drop_all()
    
class FlaskTestCase(BaseTestCase):
  """
  Making sure Flask is set up correctly
  """
  def test_index(self):
    response = self.client.get('/login', content_type = 'html/text')
    self.assertEqual(response.status_code, 200)
    
  def test_route_login(self):
    response = self.client.get('/', follow_redirects=True)
    self.assertIn('Please log in to access this page', response.data)
    
  def test_login_load(self):
    response = self.client.get('/login')
    self.assertIn(b'Please login again!', response.data)  
