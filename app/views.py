from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ConsultationRequest
from django.urls import get_resolver, reverse, NoReverseMatch

# Create your views here.

#global variables 
def global_vars(request):
    og_site_name = f'{request.user.username} from Vortfolio shares' if request.user.is_authenticated else 'Vortfolio'

    return {
        'siteName': 'Vortfolio',
        'author':'Abdullah',
        'og_site_name':og_site_name,
        'logo':'https://lh3.googleusercontent.com/pw/AP1GczOGutgra7QDYHKh6So_zvBBe7oZ17qLabQT68A4JGpN06fQ__3F47qiBBh_RmU0EhmAOdp-K9j9li5ARd97yh1UvICqt45ATlYcuoskceWPfymdTyq28YN9eK7958crO3UfRDHQE7GktH1d0r0VPzs=w575-h429-s-no-gm?authuser=0',
        'views':'Subscribers',
    }
def index(request):
    
    context = {
        'title': 'Vortfolio – Code. Create. Transform.',
        'description':'Vortfolio provides professional web development, innovative AI tools, and student-centered tech education—all in one dynamic platform.',
        'keywords':'Vortfolio, Web Development, AI Solutions, Digital Portfolio, Professional Portfolio, Vortfolio Platform, Full Stack Development',
        'og_title':'Vortfolio – Code. Create. Transform.',
        'og_description':'Vortfolio provides professional web development, innovative AI tools, and student-centered tech education—all in one dynamic platform.',
        'og_image':'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'og_image_alt':'Vortfolio',
        'og_type': 'website',
        'og_url': 'Vortfolio',

        #twitter card
        
        'twitter_card': 'summary_large_image',
        'twitter_title': 'Vortfolio – Code. Create. Transform.',
        'twitter_description': 'Vortfolio provides professional web development, innovative AI tools, and student-centered tech education—all in one dynamic platform..',
        'twitter_image': 'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'twitter_image_alt': 'Vortfolio',
        'twitter_url': 'Vortfolio',
        # 'twitter_card_type': 'summary_large_image',
        

    }
    return render(request, "index.html" ,context)
def about(request):
    context = {
        'title': 'About - Vortfolio AI Based Software Development',
        'description':'Vortfolio delivers expert web development, AI solutions, and tech education for students—empowering future professionals with next-gen digital services.',
        'keywords':'Vortfolio, Web Development, AI Solutions, Digital Portfolio, Professional Portfolio, Vortfolio Platform, Full Stack Development',
        'og_title':'About - Vortfolio AI Based Software Development',
        'og_description':'Vortfolio delivers expert web development, AI solutions, and tech education for students—empowering future professionals with next-gen digital services.',
        'og_image':'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'og_image_alt':'Vortfolio',
        'og_type': 'website',
        'og_url': request.build_absolute_uri(),

        #twitter card
        
        'twitter_card': 'summary_large_image',
        'twitter_title': 'About Vortfolio - Professional Web Development, AI & Digital Solutions Platform',
        'twitter_description': 'Vortfolio delivers expert web development, AI solutions, and tech education for students—empowering future professionals with next-gen digital services.',
        'twitter_image': 'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'twitter_image_alt': 'Vortfolio',
        'twitter_url': request.build_absolute_uri(),
        # 'twitter_card_type': 'summary_large_image',
        

    }
    return render(request, "about.html" , context)
def projects(request):
    context = {
        'title': 'Projects – Vortfolio | Web Development & AI Solutions Showcase.',
        'description':'Discover Vortfolio’s real-world projects in web development, AI, and digital solutions. See how we deliver innovation, results, and next-gen tech experiences.',
        'keywords':'Vortfolio, Web Development, AI Solutions, Digital Portfolio, Professional Portfolio, Vortfolio Platform, Full Stack Development',
        'og_title':'Projects – Vortfolio | Web Development & AI Solutions Showcase',
        'og_description':'Discover Vortfolio’s real-world projects in web development, AI, and digital solutions. See how we deliver innovation, results, and next-gen tech experiences.',
        'og_image':'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'og_image_alt':'Vortfolio',
        'og_type': 'website',
        'og_url': request.build_absolute_uri(),

        #twitter card
        
        'twitter_card': 'summary_large_image',
        'twitter_title': 'Projects – Vortfolio | Web Development & AI Solutions Showcase',
        'twitter_description': 'Discover Vortfolio’s real-world projects in web development, AI, and digital solutions. See how we deliver innovation, results, and next-gen tech experiences.',
        'twitter_image': 'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'twitter_image_alt': 'Vortfolio',
        'twitter_url': request.build_absolute_uri(),
        # 'twitter_card_type': 'summary_large_image',
        

    }
    return render(request, "projects.html",context)
def services(request):
    context = {
        'title': 'Services – Vortfolio | Web Development, AI & Digital Solutions',
        'description':'Explore Vortfolio’s expert services in web development, AI integration, and digital transformation. Scalable tech solutions for businesses and students alike.',
        'keywords':'Vortfolio, Web Development, AI Solutions, Digital Portfolio, Professional Portfolio, Vortfolio Platform, Full Stack Development',
        'og_title':'Services – Vortfolio | Web Development, AI & Digital Solutions',
        'og_description':'Explore Vortfolio’s expert services in web development, AI integration, and digital transformation. Scalable tech solutions for businesses and students alike.',
        'og_image':'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'og_image_alt':'Vortfolio',
        'og_type': 'website',
        'og_url': request.build_absolute_uri(),

        #twitter card
        
        'twitter_card': 'summary_large_image',
        'twitter_title': 'Services – Vortfolio | Web Development, AI & Digital Solutions',
        'twitter_description': 'Explore Vortfolio’s expert services in web development, AI integration, and digital transformation. Scalable tech solutions for businesses and students alike.',
        'twitter_image': 'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'twitter_image_alt': 'Vortfolio',
        'twitter_url': request.build_absolute_uri(),
        # 'twitter_card_type': 'summary_large_image',
        

    }
    return render(request, "services.html" , context)
@csrf_exempt
def contact(request):
    context = {
        'title': 'Contact Us – Vortfolio | Get in Touch for Web & AI Solutions',
        'description':'Have questions or project ideas? Contact Vortfolio for expert web development, AI solutions, and digital services. We\'re here to help you grow online.',
        'keywords':'Vortfolio, Web Development, AI Solutions, Digital Portfolio, Professional Portfolio, Vortfolio Platform, Full Stack Development',
        'og_title':'Contact Us – Vortfolio | Get in Touch for Web & AI Solutions',
        'og_description':'Have questions or project ideas? Contact Vortfolio for expert web development, AI solutions, and digital services. We\'re here to help you grow online.',
        'og_image':'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'og_image_alt':'Vortfolio',
        'og_type': 'website',
        'og_url': request.build_absolute_uri(),

        #twitter card
        
        'twitter_card': 'summary_large_image',
        'twitter_title': 'Contact Us – Vortfolio | Get in Touch for Web & AI Solutions',
        'twitter_description': 'Have questions or project ideas? Contact Vortfolio for expert web development, AI solutions, and digital services. We\'re here to help you grow online.',
        'twitter_image': 'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'twitter_image_alt':'Vortfolio',
        'twitter_url': request.build_absolute_uri(),
        # 'twitter_card_type': 'summary_large_image',
        

    }
    if request.method == 'GET':
        return render(request, 'contact.html' , context)
    
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Check if user already exists
            existing_request = ConsultationRequest.objects.filter(company_email=data['companyEmail']).first()
            
            if existing_request and not data.get('confirmUpdate') and not data.get('submitNew'):
                return JsonResponse({
                    'status': 'exists',
                    'existingData': {
                        'firstName': existing_request.first_name,
                        'lastName': existing_request.last_name,
                        'companyEmail': existing_request.company_email,
                        'phoneNumber': existing_request.phone_number
                    }
                })
            
            if existing_request and data.get('confirmUpdate'):
                # Update existing record
                existing_request.first_name = data['firstName']
                existing_request.last_name = data['lastName']
                existing_request.phone_number = data['phoneNumber']
                existing_request.company_name = data['companyName']
                existing_request.company_website = data['companyWebsite']
                existing_request.industry = data['industry']
                existing_request.company_size = data['companySize']
                existing_request.goals = data['goals']
                existing_request.need_website = data['source1']
                existing_request.need_app = data['source2']
                existing_request.need_learning = data['source3']
                existing_request.agreed_terms = data['source4']
                existing_request.get_updates = data['source5']
                existing_request.save()
            else:
                # Create new record
                ConsultationRequest.objects.create(
                    first_name=data['firstName'],
                    last_name=data['lastName'],
                    company_email=data['companyEmail'],
                    phone_number=data['phoneNumber'],
                    company_name=data['companyName'],
                    company_website=data['companyWebsite'],
                    industry=data['industry'],
                    company_size=data['companySize'],
                    goals=data['goals'],
                    need_website=data['source1'],
                    need_app=data['source2'],
                    need_learning=data['source3'],
                    agreed_terms=data['source4'],
                    get_updates=data['source5']
                )
            
            return JsonResponse({'status': 'success'})
            
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

def portfolio(request):
    context = {
        'title': 'Portfolio – Vortfolio | Web Development & AI Projects Showcase',
        'description':'Browse Vortfolio’s portfolio of custom web development, AI solutions, and digital innovations. Real-world projects that highlight creativity and results.',
        'keywords':'Vortfolio, Web Development, AI Solutions, Digital Portfolio, Professional Portfolio, Vortfolio Platform, Full Stack Development',
        'og_title':'Portfolio – Vortfolio | Web Development & AI Projects Showcase',
        'og_description':'Browse Vortfolio’s portfolio of custom web development, AI solutions, and digital innovations. Real-world projects that highlight creativity and results.',
        'og_image':'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'og_image_alt':'Vortfolio',
        'og_type': 'website',
        'og_url': request.build_absolute_uri(),

        #twitter card
        
        'twitter_card': 'summary_large_image',
        'twitter_title': 'Portfolio – Vortfolio | Web Development & AI Projects Showcase',
        'twitter_description': 'Browse Vortfolio’s portfolio of custom web development, AI solutions, and digital innovations. Real-world projects that highlight creativity and results.',
        'twitter_image': 'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'twitter_image_alt': 'Vortfolio',
        'twitter_url': request.build_absolute_uri(),
        # 'twitter_card_type': 'summary_large_image',
        

    }
    return render(request, "portfolio.html" , context)

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)
def learn(request):
    context = {
        'title': 'Learn with Vortfolio – Web, Software & AI Development Courses',
        'description':'Explore Vortfolio’s learning platform for web development, software engineering, and AI. Access beginner to advanced tutorials, roadmaps, and real-world projects.',
        'keywords':'Vortfolio, Web Development, AI Solutions, Digital Portfolio, Professional Portfolio, Vortfolio Platform, Full Stack Development',
        'og_title':'Learn with Vortfolio – Web, Software & AI Development Courses',
        'og_description':'Explore Vortfolio’s learning platform for web development, software engineering, and AI. Access beginner to advanced tutorials, roadmaps, and real-world projects.',
        'og_image':'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'og_image_alt':'Vortfolio',
        'og_type': 'website',
        'og_url': request.build_absolute_uri(),

        #twitter card
        
        'twitter_card': 'summary_large_image',
        'twitter_title': 'Learn with Vortfolio – Web, Software & AI Development Courses',
        'twitter_description': 'Explore Vortfolio’s learning platform for web development, software engineering, and AI. Access beginner to advanced tutorials, roadmaps, and real-world projects.',
        'twitter_image': 'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'twitter_image_alt': 'Vortfolio',
        'twitter_url': request.build_absolute_uri(),
        # 'twitter_card_type': 'summary_large_image',
        

    } 
    # Fix the template path by using forward slashes and removing the backslash
    return render(request, "Services/learn.html" , context)


def ads_txt(request):
    content = "google.com, pub-4959773968938981, DIRECT, f08c47fec0942fa0"
    return HttpResponse(content, content_type="text/plain")

def robots_txt(request):
    content = (
        "User-agent: *\n"
        "Disallow: /admin/\n"
        "Allow: /\n"
        "Sitemap: https://www.vortfolio.icu/sitemap.xml\n"  # Replace with your actual domain
    )
    return HttpResponse(content, content_type="text/plain")

def consultation_detail(request, id):
    consultation = get_object_or_404(ConsultationRequest, id=id)
    return render(request, 'consultation_detail.html', {'consultation': consultation})


def learning_sd(request):
    context = {
        'title': 'Learn Software Development – Vortfolio | Courses, Roadmaps & Skills',
        'description':'Master software development with Vortfolio’s beginner-friendly guides, learning paths, and practical projects. Start coding and build real-world applications today.',
        'keywords':'Vortfolio, Web Development, AI Solutions, Digital Portfolio, Professional Portfolio, Vortfolio Platform, Full Stack Development, Learn Web Development, Learn AI, Learn Digital Solutions',
        #og tags
        'og_title':'Learn Software Development – Vortfolio | Courses, Roadmaps & Skills',
        'og_description':'Master software development with Vortfolio’s beginner-friendly guides, learning paths, and practical projects. Start coding and build real-world applications today.',
        'og_image':'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'og_image_alt':'Vortfolio',
        'og_type': 'website',
        'og_url': request.build_absolute_uri(),

        #twitter card
        
        'twitter_card': 'summary_large_image',
        'twitter_title': 'Learn Software Development – Vortfolio | Courses, Roadmaps & Skills',
        'twitter_description': 'Master software development with Vortfolio’s beginner-friendly guides, learning paths, and practical projects. Start coding and build real-world applications today.',
        'twitter_image': 'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'twitter_image_alt': 'Vortfolio',
        'twitter_url': request.build_absolute_uri(),
        # 'twitter_card_type': 'summary_large_image',
    }
    return render(request, 'Services/learn_Software_development.html' , context)

def roadmap(request):
    context = {
        'title': 'Roadmap – Vortfolio | Web Development & AI Projects Showcase',
        'description':'Browse Vortfolio’s portfolio of custom web development, AI solutions, and digital innovations. Real-world projects that highlight creativity and results.',
        'keywords':'Vortfolio, Web Development, AI Solutions, Digital Portfolio, Professional Portfolio, Vortfolio Platform, Full Stack Development',
        'og_title':'Web Development Roadmap – Vortfolio | Learn & Build Like a Pro',
        'og_description':'Explore Vortfolio’s complete web development roadmap—from HTML and CSS to advanced frameworks and deployment. Ideal for students, beginners, and aspiring developers.',
        'og_image':'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'og_image_alt':'Vortfolio',
        'og_type': 'website',
        'og_url': request.build_absolute_uri(),

        #twitter card
        
        'twitter_card': 'summary_large_image',
        'twitter_title': 'Web Development Roadmap – Vortfolio | Learn & Build Like a Pro',
        'twitter_description': 'Explore Vortfolio’s complete web development roadmap—from HTML and CSS to advanced frameworks and deployment. Ideal for students, beginners, and aspiring developers.',
        'twitter_image': 'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'twitter_image_alt': 'Vortfolio',
        'twitter_url': request.build_absolute_uri(),
        # 'twitter_card_type': 'summary_large_image',
        

    } 
    return render(request, 'Services/roadmap.html', context)

def privacy_policy(request):
    context = {
        'title': 'Privacy Policy – Vortfolio | Your Data, Our Commitment',
        'description':'Vortfolio is committed to protecting your privacy. Read our policy to understand how we collect, use, and safeguard your information.',
        'keywords':'Vortfolio, Privacy Policy, Data Protection, User Privacy, Information Security',

        'og_title':'Privacy Policy – Vortfolio | Your Data, Our Commitment',
        'og_description':'Vortfolio is committed to protecting your privacy. Read our policy to understand how we collect, use, and safeguard your information.',
        'og_image':'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'og_image_alt':'Privacy Policy',
        'og_type': 'website',
        'og_url': request.build_absolute_uri(),
        #twitter card
        'twitter_card': 'summary_large_image',
        'twitter_title': 'Privacy Policy – Vortfolio | Your Data, Our Commitment',
        'twitter_description':'Vortfolio is committed to protecting your privacy. Read our policy to understand how we collect, use, and safeguard your information.',
        'twitter_image':'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'twitter_image_alt':'Privacy Policy',
        'twitter_url': request.build_absolute_uri(),

    }

    return render(request, 'privacy_policy.html', context)
from django.http import HttpResponse

def serve_txt_file(request):
    content = "bca6356bcc6f4e32986944a2297de9e7"
    return HttpResponse(content, content_type="text/plain")

def dynamic_sitemap(request):
    urls = []
    for name in get_resolver().reverse_dict.keys():
        if isinstance(name, str):  # Ensure it's a named URL
            try:
                # Attempt to reverse the URL
                url = request.build_absolute_uri(reverse(name))
                urls.append(f"<url><loc>{url}</loc></url>")
            except NoReverseMatch:
                # Skip URLs that require arguments
                continue

    sitemap_content = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"{''.join(urls)}"
        "</urlset>"
    )
    return HttpResponse(sitemap_content, content_type="application/xml")


def html(request):
    context = {
        'title': 'HTML – Vortfolio | Learn HTML Basics and Beyond',
        'description':'Master HTML with Vortfolio’s beginner-friendly guides, tutorials, and projects. Start coding your web pages today!',
        'keywords':'Vortfolio, HTML, Web Development, Coding, Tutorials',

        'og_title':'HTML – Vortfolio | Learn HTML Basics and Beyond',
        'og_description':'Master HTML with Vortfolio’s beginner-friendly guides, tutorials, and projects. Start coding your web pages today!',
        'og_image':'https://lh3.googleusercontent.com/pw/AP1GczNQtl4jq0_KvSNForDs2G7k7nurE0k48-4wQBWLJ-fN41WyXur-d_NXnuKer1lLZ8aVKu43M8Bs6uoU5ANoIS0Ce-3Nk8y9PKN8oXjq0I_uwVG0DPYduFFw22tAxC9LDJTdEKnv8vrvL3yOT2pIqNK0=w700-h420-s-no-gm?authuser=0',
        'og_image_alt':'HTML Guide',
        'og_type': 'website',
        'og_url': request.build_absolute_uri(),
        #twitter card
        'twitter_card': 'summary_large_image',
        'twitter_title': 'HTML – Vortfolio | Learn HTML Basics and Beyond',
        'twitter_description':'Master HTML with Vortfolio’s beginner-friendly guides, tutorials, and projects. Start coding your web pages today!',
        'twitter_image':'https://lh3.googleusercontent.com/pw/AP1GczNQtl4jq0_KvSNForDs2G7k7nurE0k48-4wQBWLJ-fN41WyXur-d_NXnuKer1lLZ8aVKu43M8Bs6uoU5ANoIS0Ce-3Nk8y9PKN8oXjq0I_uwVG0DPYduFFw22tAxC9LDJTdEKnv8vrvL3yOT2pIqNK0=w700-h420-s-no-gm?authuser=0',
        'twitter_image_alt':'HTML Guide',
        'twitter_url': request.build_absolute_uri(),

    }
    return render(request, "Services/html.html", context)


def appdev(request):
    context = {
        'title': 'App Development Experts: Building High-Performance Mobile & Web Apps',
        'description':'We specialize in app development for mobile and web platforms, delivering high-performance, scalable, and user-friendly applications. Our services include native, cross-platform, and progressive web apps with a focus on usability, functionality, and seamless user experience',
        'keywords':'Vortfolio, HTML, Web Development, Coding, Tutorials, app development, mobile app development, web app development, native apps, cross-platform apps, iOS app development, Android app development, progressive web apps, PWA, Flutter development, React Native development, backend development, frontend development, app UI design, app UX design, user interface, user experience, mobile app design, responsive design, scalable apps, custom apps, enterprise app development, startup app development, app testing, app prototyping, app deployment, app maintenance, API integration, cloud apps, SaaS apps, app performance optimization, interactive apps, app features, mobile development, software development, app security, app analytics, mobile UX, mobile UI, app monetization, app store optimization, app marketing, agile development, app lifecycle, app design, UI/UX for apps, app frameworks, app development tools, app updates, real-time apps, app scalability, app design patterns, hybrid apps, native mobile apps, cross-platform mobile apps, React Native apps, Flutter apps, Swift apps, Kotlin apps, Java apps, app development services, mobile solutions, app prototyping tools, app development trends, app development best practices',

        'og_title':'App Development Experts: Building High-Performance Mobile & Web Apps',
        'og_description':'We specialize in app development for mobile and web platforms, delivering high-performance, scalable, and user-friendly applications. Our services include native, cross-platform, and progressive web apps with a focus on usability, functionality, and seamless user experience',
        'og_image':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTH2q74ynQYljmXDJqQZ4P4gcqupLpwQXWIWg&s',
        'og_image_alt':'App dev Guide',
        'og_type': 'website',
        'og_url': request.build_absolute_uri(),
        #twitter card
        'twitter_card': 'summary_large_image',
        'twitter_title': 'App Development Experts: Building High-Performance Mobile & Web Apps',
        'twitter_description':'We specialize in app development for mobile and web platforms, delivering high-performance, scalable, and user-friendly applications. Our services include native, cross-platform, and progressive web apps with a focus on usability, functionality, and seamless user experience',
        'twitter_image':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTH2q74ynQYljmXDJqQZ4P4gcqupLpwQXWIWg&s',
        'twitter_image_alt':'App dev Guide',
        'twitter_url': request.build_absolute_uri(),

    }
    return render(request, "app-development.html", context)



def uiux(request):
    context = {
        'title': 'Crafting Seamless UI/UX Solutions',
        'description':'Expert UI/UX design services focused on crafting visually stunning and highly intuitive digital interfaces for seamless user experiences . Delivering innovative UI/UX solutions that prioritize user needs, enhance interaction, and improve overall satisfaction across web and mobile platforms.',
        'keywords':'Vortfolio, UI/UX Design, Web Development, Coding, Tutorials , UI design, UX design, user interface, user experience, interaction design, interface design, usability, wireframes, prototypes, mobile app design, web design, responsive design, app design, digital design, creative design, UX research, user testing, visual design, human-centered design, experience design, information architecture, interaction flow, design system, usability testing, interface prototyping, UX strategy, product design, user journey, accessibility design, visual hierarchy, UI components, design thinking, design patterns, interface optimization, responsive UI, website UX, user-centered design, app interface, design interface, experience optimization, UI/UX development, interface usability, user engagement, UI prototyping, mobile UX, web UX, interactive design, UX analysis, UX optimization, product interface, intuitive design, interaction flow design, aesthetic design, digital experience, task flows, interface usability testing, design improvement, user interface patterns, app usability, UX best practices, UI best practices, UI trends, UX trends, interface layout, visual storytelling, interaction patterns, user satisfaction, UX evaluation, user flow, UX journey, interface design principles, accessibility standards, cross-platform design, UX prototyping, human-computer interaction, UI guidelines, UX design process, UI development, UX tools, digital product design, usability improvement, interface responsiveness, user-centric design, UX case study, UI inspiration, UX inspiration, interface aesthetics, design consistency, interaction consistency, UX research methods, UI accessibility, UX accessibility, interactive UI, engaging UX, mobile interface design, desktop UI, web application UX, software interface design, user behavior analysis',

        'og_title':'Crafting Seamless UI/UX Solutions',
        'og_description':'Expert UI/UX design services focused on crafting visually stunning and highly intuitive digital interfaces for seamless user experiences . Delivering innovative UI/UX solutions that prioritize user needs, enhance interaction, and improve overall satisfaction across web and mobile platforms.',
        'og_image':'https://img.freepik.com/free-vector/gradient-ui-ux-background_23-2149052117.jpg',
        'og_image_alt':'UI / UX Guide',
        'og_type': 'website',
        'og_url': request.build_absolute_uri(),
        #twitter card
        'twitter_card': 'summary_large_image',
        'twitter_title': 'HTML – Vortfolio | Learn HTML Basics and Beyond',
        'twitter_description':'Expert UI/UX design services focused on crafting visually stunning and highly intuitive digital interfaces for seamless user experiences . Delivering innovative UI/UX solutions that prioritize user needs, enhance interaction, and improve overall satisfaction across web and mobile platforms.',
        'twitter_image':'https://img.freepik.com/free-vector/gradient-ui-ux-background_23-2149052117.jpg',
        'twitter_image_alt':'UI / UX Guide',
        'twitter_url': request.build_absolute_uri(),

    }
    return render(request, "ui-ux-designs.html", context)


def webdev(request):
    context = {
        'title': 'Modern Web Solutions for the Modern World – Vortfolio',
        'description':'High-performance web development with AI for growing or established brands. We create scalable, secure, and future-ready websites using modern technologies',
        'keywords':'Vortfolio, HTML, Web Development, Coding, Tutorials ,web development, website development, web design, ui ux design, front end development, backend development, full stack development, responsive web design, mobile friendly websites, ecommerce website development, wordpress development, custom website design, modern web design, business website, landing page design, website redesign, web application development, custom web applications, software development, html, css, javascript, react development, next js development, node js development, python development, django development, flask development, php development, laravel development, vue js development, angular development, bootstrap websites, tailwind css websites, seo friendly website, website maintenance, website optimization, speed optimization, website performance, api development, database integration, cloud hosting, web hosting, website deployment, digital agency, creative agency, website builder service, professional web design, branding and design, ui design, ux design, interface design, logo design, creative web solutions, web design company, website development company, professional web developers, custom coding, custom themes, custom plugins, dashboard development, admin panel development, cms development, wordpress customization, shopify development, ecommerce store design, online business website, portfolio website, business landing page, startup websites, corporate website design, business branding, online presence, digital marketing integration, seo optimization, on page seo, meta tags optimization, sitemaps creation, google analytics integration, website security, ssl installation, secure website, bug fixing, website migration, domain setup, cloudflare setup, github deployment, vercel deployment, render deployment, azure deployment, aws deployment, modern ui design, creative interface design, custom animations, hero section design, website content writing, ux research, wireframing, prototyping, web consultancy, mobile app ui design, interface optimization, dark mode design, light mode design, modern typography, website color palette, minimal web design, clean web design, professional websites, creative websites, fast loading websites, high converting landing pages, call to action optimization, user engagement design, web accessibility, website testing, quality assurance, performance testing, cross browser compatibility, mobile optimization, website upgrade, digital transformation, tech solutions, scalable web apps, enterprise web solutions, custom dashboards, analytics dashboards, data visualization websites, ai integrated websites, chatbot integration, automation websites, crm integration.',

        'og_title':'Modern Web Solutions for the Modern World – Vortfolio',
        'og_description':'High-performance web development for growing brands. We create scalable, secure, and future-ready websites using modern technologies!',
        'og_image':'https://wearedevelopers.imgix.net/magazine/articles/581/images/hero/ciMw4oPCTP0xxfAT0FK0-1745839625.jpeg?w=720&auto=compress,format',
        'og_image_alt':'Web Development Services',
        'og_type': 'website',
        'og_url': 'https://www.vortfolio.icu/webdev',
        #twitter card
        'twitter_card': 'summary_large_image',
        'twitter_title': 'Modern Web Solutions for the Modern World – Vortfolio',
        'twitter_description':'High-performance web development with AI for growing or established brands. We create scalable, secure, and future-ready websites using modern technologies',
        'twitter_image':'https://wearedevelopers.imgix.net/magazine/articles/581/images/hero/ciMw4oPCTP0xxfAT0FK0-1745839625.jpeg?w=720&auto=compress,format',
        'twitter_image_alt':'Web Development Services',
        'twitter_url': 'https://www.vortfolio.icu/webdev',

    }
    return render(request, "web-development.html", context)

def aidev(request):
    context = {
        'title': 'AI Development Experts: Building Intelligent & Scalable AI Solutions',
        'description':'We provide advanced AI development services, creating intelligent, scalable, and efficient solutions for businesses. From machine learning models and natural language processing to computer vision and AI-powered automation, we deliver cutting-edge AI applications that drive innovation and optimize processes.',
        'keywords':'Vortfolio, HTML, Web Development, Coding, Tutorials , AI development, artificial intelligence, machine learning, deep learning, natural language processing, NLP, computer vision, AI solutions, AI applications, predictive analytics, AI models, neural networks, AI automation, intelligent systems, AI consulting, AI software development, AI integration, AI tools, AI frameworks, TensorFlow, PyTorch, Keras, scikit-learn, AI algorithms, AI research, AI for business, AI consulting services, AI innovation, AI project development, AI optimization, AI deployment, AI strategy, AI cloud solutions, AI SaaS, AI chatbot, AI virtual assistant, AI predictive modeling, AI image recognition, AI data analysis, AI workflow automation, AI development trends, AI use cases, AI for startups, AI for enterprises, AI programming, AI APIs, AI pipelines, AI solutions architecture, AI-powered applications, intelligent automation, AI research and development, AI services, AI-driven business solutions, AI design, AI model training, AI model evaluation, AI deployment strategy, AI lifecycle, AI tools for developers, AI for mobile apps, AI for web apps, AI consulting solutions, AI optimization techniques, AI project management, AI solutions design, AI development process, AI model integration, AI platform development',

        'og_title':'AI Development Experts: Building Intelligent & Scalable AI Solutions',
        'og_description':'We provide advanced AI development services, creating intelligent, scalable, and efficient solutions for businesses. From machine learning models and natural language processing to computer vision and AI-powered automation, we deliver cutting-edge AI applications that drive innovation and optimize processes.',
        'og_image':'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'og_image_alt':'HTML Guide',
        'og_type': 'website',
        'og_url': request.build_absolute_uri(),
        #twitter card
        'twitter_card': 'summary_large_image',
        'twitter_title': 'AI Development Experts: Building Intelligent & Scalable AI Solutions',
        'twitter_description':'We provide advanced AI development services, creating intelligent, scalable, and efficient solutions for businesses. From machine learning models and natural language processing to computer vision and AI-powered automation, we deliver cutting-edge AI applications that drive innovation and optimize processes.',
        'twitter_image':'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'twitter_image_alt':'HTML Guide',
        'twitter_url': request.build_absolute_uri(),

    }
    return render(request, "ai-development.html", context)


def css(request):
    
    context = {
        'title': 'Mastering CSS: Styling the Web with Precision',
        'description':'Learn CSS with this complete guide to styling web pages, responsive layouts, and modern web design techniques. Ideal for beginners and developers.',
        'keywords':'CSS tutorial, learn CSS, what is CSS, CSS for beginners, CSS examples, CSS layout, responsive design CSS, Flexbox CSS, CSS Grid layout, CSS styling, web design CSS, modern CSS techniques, HTML and CSS, Cascading Style Sheets, front-end development, web development, CSS animations, CSS best practices, CSS tips and tricks, CSS selectors',
        'og_title':'Mastering CSS: Styling the Web with Precision',
        'og_description':'Learn CSS with this complete guide to styling web pages, responsive layouts, and modern web design techniques. Ideal for beginners and developers.',
        'og_image':'https://lh3.googleusercontent.com/pw/AP1GczNAu6S1jiu6yEWFCyIFzFsk0t7zw4A1a1Vzxp8otdxDoZnIRX1DGyICFbK46S5BadGqujkZ247_R9P22e-dGZTPmxdeuvW6Yju65olxmeyxUkU1y15mlsMStDXjBZ4o4dK27LAy7b8kNHtWcQeuE7Gh=w607-h250-s-no-gm?authuser=0',
        'og_image_alt':'Vortfolio',
        'og_type': 'website',
        'og_url': 'Vortfolio',

        #twitter card
        
        'twitter_card': 'summary_large_image',
        'twitter_title': 'Mastering CSS: Styling the Web with Precision',
        'twitter_description': 'Learn CSS with this complete guide to styling web pages, responsive layouts, and modern web design techniques. Ideal for beginners and developers.',
        'twitter_image': 'https://lh3.googleusercontent.com/pw/AP1GczNAu6S1jiu6yEWFCyIFzFsk0t7zw4A1a1Vzxp8otdxDoZnIRX1DGyICFbK46S5BadGqujkZ247_R9P22e-dGZTPmxdeuvW6Yju65olxmeyxUkU1y15mlsMStDXjBZ4o4dK27LAy7b8kNHtWcQeuE7Gh=w607-h250-s-no-gm?authuser=0',
        'twitter_image_alt': 'Learn CSS',
        'twitter_url': 'Vortfolio',
        # 'twitter_card_type': 'summary_large_image',
        

    }
    return render(request, "css.html" ,context)



def tech(request):
    return render (request, "Pages/techonologies details/technologies.html")
