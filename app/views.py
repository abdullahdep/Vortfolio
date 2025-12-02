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
        'title': 'HTML – Vortfolio | Learn HTML Basics and Beyond',
        'description':'Master HTML with Vortfolio’s beginner-friendly guides, tutorials, and projects. Start coding your web pages today!',
        'keywords':'Vortfolio, HTML, Web Development, Coding, Tutorials',

        'og_title':'HTML – Vortfolio | Learn HTML Basics and Beyond',
        'og_description':'Master HTML with Vortfolio’s beginner-friendly guides, tutorials, and projects. Start coding your web pages today!',
        'og_image':'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'og_image_alt':'HTML Guide',
        'og_type': 'website',
        'og_url': request.build_absolute_uri(),
        #twitter card
        'twitter_card': 'summary_large_image',
        'twitter_title': 'HTML – Vortfolio | Learn HTML Basics and Beyond',
        'twitter_description':'Master HTML with Vortfolio’s beginner-friendly guides, tutorials, and projects. Start coding your web pages today!',
        'twitter_image':'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'twitter_image_alt':'HTML Guide',
        'twitter_url': request.build_absolute_uri(),

    }
    return render(request, "app-development.html", context)



def uiux(request):
    context = {
        'title': 'HTML – Vortfolio | Learn HTML Basics and Beyond',
        'description':'Master HTML with Vortfolio’s beginner-friendly guides, tutorials, and projects. Start coding your web pages today!',
        'keywords':'Vortfolio, HTML, Web Development, Coding, Tutorials',

        'og_title':'HTML – Vortfolio | Learn HTML Basics and Beyond',
        'og_description':'Master HTML with Vortfolio’s beginner-friendly guides, tutorials, and projects. Start coding your web pages today!',
        'og_image':'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'og_image_alt':'HTML Guide',
        'og_type': 'website',
        'og_url': request.build_absolute_uri(),
        #twitter card
        'twitter_card': 'summary_large_image',
        'twitter_title': 'HTML – Vortfolio | Learn HTML Basics and Beyond',
        'twitter_description':'Master HTML with Vortfolio’s beginner-friendly guides, tutorials, and projects. Start coding your web pages today!',
        'twitter_image':'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'twitter_image_alt':'HTML Guide',
        'twitter_url': request.build_absolute_uri(),

    }
    return render(request, "ui-ux-designs.html", context)


def webdev(request):
    context = {
        'title': 'HTML – Vortfolio | Learn HTML Basics and Beyond',
        'description':'Master HTML with Vortfolio’s beginner-friendly guides, tutorials, and projects. Start coding your web pages today!',
        'keywords':'Vortfolio, HTML, Web Development, Coding, Tutorials',

        'og_title':'HTML – Vortfolio | Learn HTML Basics and Beyond',
        'og_description':'Master HTML with Vortfolio’s beginner-friendly guides, tutorials, and projects. Start coding your web pages today!',
        'og_image':'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'og_image_alt':'HTML Guide',
        'og_type': 'website',
        'og_url': request.build_absolute_uri(),
        #twitter card
        'twitter_card': 'summary_large_image',
        'twitter_title': 'HTML – Vortfolio | Learn HTML Basics and Beyond',
        'twitter_description':'Master HTML with Vortfolio’s beginner-friendly guides, tutorials, and projects. Start coding your web pages today!',
        'twitter_image':'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'twitter_image_alt':'HTML Guide',
        'twitter_url': request.build_absolute_uri(),

    }
    return render(request, "web-development.html", context)

def aidev(request):
    context = {
        'title': 'HTML – Vortfolio | Learn HTML Basics and Beyond',
        'description':'Master HTML with Vortfolio’s beginner-friendly guides, tutorials, and projects. Start coding your web pages today!',
        'keywords':'Vortfolio, HTML, Web Development, Coding, Tutorials',

        'og_title':'HTML – Vortfolio | Learn HTML Basics and Beyond',
        'og_description':'Master HTML with Vortfolio’s beginner-friendly guides, tutorials, and projects. Start coding your web pages today!',
        'og_image':'https://lh3.googleusercontent.com/pw/AP1GczPbTAZex5suqg2OTqAEB4mUhR2QzwDNSxgzWFuDi5H6GuDk8aI4zSo6JVddIAYzhB7pAwUVtDEF2kGGT_flUpQsB8-Tp2YXRcgYYJhdBg7bPNHdlaI5SgtmrFtPmQnQgPKjN3ZhRszmzyP9VR_6kN0=w575-h429-s-no-gm?authuser=0',
        'og_image_alt':'HTML Guide',
        'og_type': 'website',
        'og_url': request.build_absolute_uri(),
        #twitter card
        'twitter_card': 'summary_large_image',
        'twitter_title': 'HTML – Vortfolio | Learn HTML Basics and Beyond',
        'twitter_description':'Master HTML with Vortfolio’s beginner-friendly guides, tutorials, and projects. Start coding your web pages today!',
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
