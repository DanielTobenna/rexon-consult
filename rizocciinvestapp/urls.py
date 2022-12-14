from django.urls import path

from . import views

urlpatterns=[
	path('', views.home, name='home'),
	path('what/', views.what, name='what'),
	path('plans/', views.plans, name='plans'),
	path('approach/', views.approach, name='approach'),
	path('investors/', views.investors, name='investors'),
	path('how/', views.how, name='how'),
	path('nfp/', views.nfp, name='nfp'),
	path('who/', views.who, name='who'),
	path('aml/', views.aml, name='aml'),
	path('news/', views.news, name='news'),
	path('about/', views.about, name='about'),
	path('contact/', views.contact, name='contact'),
	path('services/', views.services, name='services'),
	path('signin/', views.signin, name='signin'),
	path('main-view/', views.main_view, name='main-view'),
	path('main-view/<str:ref_code>/', views.main_view, name='main-view'),
	path('signup/', views.signup, name='signup'),
	path('faq/', views.faq, name='faq'),
	path('affiliate/', views.affiliate, name='affiliate'),
	path('representatives/', views.representatives, name='representatives'),
	path('bounty/', views.bounty, name='bounty'),
	path('terms/', views.terms, name='terms'),
	path('privacy/', views.privacy, name='privacy'),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('deposit/', views.deposit, name='deposit'),
	path('withdrawal/', views.withdrawal, name='withdrawal'),
	path('history/', views.history, name='history'),
	path('myreferals/', views.myreferals, name='myreferals'),
	path('confirm_withdrawal/', views.confirm_withdrawal, name='confirm_withdrawal' ),
	path('update_withdrawal/<str:pk>/', views.update_withdrawal, name='update_withdrawal' ),
	path('confirm_deposit/', views.confirm_deposit, name='confirm_deposit' ),
	path('update_payment/<str:pk>/', views.update_payment, name='update_payment' ),
	path('account_settings/', views.account_settings, name='account_settings'),
	path('ref_link/', views.reflink, name='ref_link'),
	path('logout/', views.logoutuser, name='logout')
]