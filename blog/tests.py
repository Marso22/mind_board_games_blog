from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, Comment

class CommentSubmissionTest(TestCase):
    """
    Automated tests for comment functionality, authentication, page loads, and admin access.
    """

    def setUp(self):
        """
        Create a test user and a test post for use in all tests.
        """
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            content='Test content',
            status=1,
            author=self.user,
        )

    def test_comment_submission_shows_message(self):
        """
        Test that a logged-in user can submit a comment and sees a success message.
        """
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(
            reverse('post_detail', args=[self.post.slug]),
            {'body': 'Test comment'},
            follow=True
        )
        self.assertContains(response, 'Comment submitted and awaiting approval')
        self.assertEqual(Comment.objects.count(), 1)

    def test_anonymous_comment_submission_fails(self):
        """
        Test that an anonymous user cannot submit a comment.
        """
        response = self.client.post(
            reverse('post_detail', args=[self.post.slug]),
            {'body': 'Anonymous comment'},
            follow=True
        )
        self.assertNotContains(response, 'Comment submitted and awaiting approval')
        self.assertEqual(Comment.objects.count(), 0)

    def test_empty_comment_not_saved(self):
        """
        Test that an empty comment is not saved.
        """
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(
            reverse('post_detail', args=[self.post.slug]),
            {'body': ''},
            follow=True
        )
        self.assertNotContains(response, 'Comment submitted and awaiting approval')
        self.assertEqual(Comment.objects.count(), 0)

    def test_post_detail_page_loads(self):
        """
        Test that the post detail page loads successfully.
        """
        response = self.client.get(reverse('post_detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)

    def test_user_registration_and_login(self):
        """
        Test user registration and login flows.
        """
        response = self.client.post(reverse('account_signup'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'StrongPassword123',
            'password2': 'StrongPassword123',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after signup
        user_exists = User.objects.filter(username='newuser').exists()
        self.assertTrue(user_exists)

        login_response = self.client.post(reverse('account_login'), {
            'login': 'newuser',
            'password': 'StrongPassword123',
        })
        self.assertEqual(login_response.status_code, 302)  # Redirect after login

    def test_unapproved_comment_not_visible(self):
        """
        Test that unapproved comments are not visible on the post detail page.
        """
        self.client.login(username='testuser', password='testpass')
        self.client.post(
            reverse('post_detail', args=[self.post.slug]),
            {'body': 'Needs approval'},
            follow=True
        )
        response = self.client.get(reverse('post_detail', args=[self.post.slug]))
        self.assertNotContains(response, 'Needs approval')

    def test_home_page_loads(self):
        """
        Test that the home page loads successfully.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_loads(self):
        """
        Test that the about page loads successfully.
        """
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_admin_login(self):
        """
        Test that an admin user can log in and access the admin interface.
        """
        admin = User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')
        login = self.client.login(username='admin', password='adminpass')
        self.assertTrue(login)
        response = self.client.get(reverse('admin:index'))
        self.assertEqual(response.status_code, 200)
