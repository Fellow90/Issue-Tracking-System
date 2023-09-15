from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView, ListView
from django.contrib.auth.views import LogoutView 
from django.urls import reverse_lazy

from issue.forms import RegistrationForm, LoginForm, TicketForm, ProfileForm, CommentForm
from issue.models import CustomUser, Ticket, Comment

class UserRegistrationView(CreateView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')

class UserLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm 

    def get_success_url(self):
        return reverse_lazy('profile')

class UserProfileView(UpdateView, DetailView):
    model = CustomUser
    form_class = ProfileForm
    template_name = 'profile.html'
    context_object_name = 'user' 
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('login')
    
class TicketListView(ListView):
    model = Ticket
    template_name = 'ticket_list.html'
    context_object_name = 'user_tickets'

    def get_queryset(self):
        return Ticket.objects.filter(issuer = self.request.user)

class TicketCreateView(CreateView):
    model = Ticket
    form_class = TicketForm
    context_object_name = 'ticket'
    template_name = 'ticket_create.html'

    def get_queryset(self):
        return Ticket.objects.filter(issuer = self.request.user)  

    def form_valid(self, form):
        form.instance.issuer = self.request.user
        form.instance.assigned_to = 'L1'
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('ticket_detail', kwargs={'pk': self.object.pk})

    

class TicketDetailView(UpdateView,DetailView):
    model = Ticket
    form_class = TicketForm
    template_name = 'ticket_detail.html' 
    context_object_name = 'ticket' 

    def get_queryset(self):
        return Ticket.objects.filter(issuer = self.request.user)

    def get_success_url(self):
        return reverse_lazy('ticket_detail', kwargs={'pk': self.object.pk})
    


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    context_object_name = 'comments'
    template_name = 'comment_create.html'

    def get_queryset(self):
        kwargs = {'pk' : self.object.pk}   
        return Comment.objects.filter(ticket__pk = kwargs.get('pk'))

    def form_valid(self, form):
        ticket_pk = self.kwargs.get('pk')
        ticket = Ticket.objects.get(id = ticket_pk)
        form.instance.issuer = self.request.user
        form.instance.ticket = ticket
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ticket'] = Ticket.objects.get(pk = self.kwargs['pk'])
        return context
    
    def get_success_url(self):
        return reverse_lazy('comments', kwargs={'pk': self.object.ticket.pk})
    
    
class CommentListView(ListView): 
    model = Comment
    template_name = 'comment_list.html'
    context_object_name = 'comments'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ticket_pk = self.kwargs.get('pk')
        context['ticket'] = Ticket.objects.get(pk=ticket_pk) 
        return context
    

    def get_queryset(self):
        ticket_pk = self.kwargs.get('pk')
        return Comment.objects.filter(ticket__pk= ticket_pk)

    
    