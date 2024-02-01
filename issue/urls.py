from django.urls import path
from issue.views import UserRegistrationView, UserLoginView, UserProfileView, UserLogoutView,TicketListView,TicketCreateView, TicketDetailView, CommentCreateView, CommentListView, L1SupportTicketListView
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('tickets/create/', TicketCreateView.as_view(), name='ticket_create'),
    path('tickets/',TicketListView.as_view(),name='tickets'),
    path('tickets/<int:pk>/', TicketDetailView.as_view(), name='ticket_detail'),
    path('tickets/<int:pk>/comments/create/',CommentCreateView.as_view(), name = 'create_comment'),
    path('tickets/<int:pk>/comments/',CommentListView.as_view(), name = 'comments'),
    path('l1/tickets/',L1SupportTicketListView.as_view(),name='l1supportticket'),

]
