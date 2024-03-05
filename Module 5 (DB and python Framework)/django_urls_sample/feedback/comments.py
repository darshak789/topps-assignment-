'''
10 Forms:
Starting setup:
    -admin panel provides admin to enter data not to user.
    -user can review some product.-> created app review
    -create template directory in review then repeat app and at last create review.html
    -not extending base.html
    -generating url at global  level in urls.py
    -register app
    -create urls.py in review app and import views file
    -create html file review in review directory

Adding a dummy form:
    -created form simple form tag.
    -id and for should be equal to correlate and name attribute is associated with data entered.
    
    request in views:

    In Django views, the request is a parameter passed to your view function. It represents the current HTTP request that your view is processing.
    It's an instance of the HttpRequest class but is often referred to simply as request.
    It contains information about the current request, such as GET and POST parameters, cookies, session data, and more.
    
    HttpRequest class:

    The HttpRequest class is part of Django's HTTP handling framework.
    It is not typically used directly in your code unless you are building a middleware or custom components.
    In views, you receive an instance of this class as the request parameter
    
    HttpResponse class:

    The HttpResponse class is used to construct an HTTP response.
    When your view is executed, you create an instance of HttpResponse and return it.
    You can pass content, status codes, headers, and other information to the HttpResponse instance.
    
    In summary, request is the current HTTP request passed to your view, 
    HttpResponse is the response your view generates, and
    HttpRequest is the class representing the incoming HTTP request. 
    You generally work with request and HttpResponse in your views, and 
    the HttpRequest class is more often used internally by Django itself.

Get and Post request:
    -a button by default submits a form i.e. type="submit". can explicitly submit .
        try giving type="button"
    -what does a submitting form mean?
        it means by default the browser will construct a new http request which is sent to server that served at this form.
        When the user clicks the submit button,
        the form is submitted to the URL specified in the action attribute of the form tag. 
        In this case, it's the same URL ("/") because no specific URL is provided.
        
    -get request in laymen temrs means, i want to get some data.therefor if you enter url in your address bar 
        that will always send get request to the server.
        can check by go to Network tab and can see all the request being sent.
        can see html code in response which is sent back
        click on header ->general : request method: get
        if we entered a data then new request will send sent which is http:..../?username=abhi
    -post: collected some data and now we want to send to server
        sending a post request make it clear that you are submitting data and this request is not just about 
        getting data.
        so need to change form element to send a post request instead of get
    -add method attribute in form as POST
        this will send post request when this form is submitted
        csrf token error will raise and notice that question mark thing wont show up
        at bottom there is form data. post request unlike get can carry data

CSRF token:
    -cross site request forgery.its about builiding request which look like valid but aren't.
    - i tricked user to visit my page which is similar to official bankk's site.
        then user will fill data and i will slightlt replace data such as changing name and send to original bank's server.
        then money will be transferred to me instead of desired person. thats how i build malicious server.
        thats where django csrf security feautures comes to picture.
        in our website we add dynamically generated token to our generated forms and that token has to be sent together with post request to our server.
        if someone fakes our website that token will be missing and only official server,our application knows how to build that token  and how a valid token should look like because that token is generated on the server
        so check that every incoming request consist valid token and accept it.
    -add a csrf token
    -check inspect
    
Handling form submission and extracting data:
    -how can we utilized that submitted data?
    -go to views py file because thats where ultimately request is handled .
        review function get triggered in both cases of get and post
        we can also change the url to which your post request is sent.
        back in form beside method add action. this allows you to spiecify the path after your domain to which this request should be sent.
        try setting to "/". it will be standard url which is already being sent.
            http://127.0.0.1:8000/ SAME AS BEFORE.
        so omitting is same before. hitting submit will cause arrival at review function
    -we are getting post and get request on review function and it is rendering same page.we can send different page for post reuqest
    -method gives us access to the method that was used for submitting data and .post gives us data itself
        Post will hold dictionary where the keys are names set on the inputs in the form
    -we can return reviews/thank_you.html for post request
        but typically we dont want to send html code for post request because post request is meant for submitting data to the server not to get some page
        so we will redirect to different url with a  get request and that different url will then a render template.
    -Django will automatically append a trailing slash to the URLs if you use the APPEND_SLASH setting (which is True by default in Django).  
        
Manual form validation & the problems with _that_:
    - curently we are fetching data and printing it.
    -typically we want to validate it.i.e check whether the student entered a valid data
    - if you directly hit submit its still works
    -we can make sure that username is not empty
    -handling a form manually results lot of work i.e. username should not be empty-> update views.py and also review.html to print context
    -
        {% if has_error %}
            <p>Enter a valid data</p>
        {% endif %}
        
        if entered_username == "":
            return render(request,'reviews/review.html',{"has_error":True})  # added false for get request so that dtl wont executed
    -for that django provides django for class
    
Using the django form class:
    -creating a new file forms py and creating class that defines shape of our forms
        and the different input we want and validation rule for that inputs
        convention that end with Form
        fields are similar to fields of models but we are not defining any database model
        we can use form.cleaned_data to write into database
    -created user_name field
    -importing class in view.py file
    -{{form }} automatically render input type and label 
    
    
Validation with django forms:
    -if data is not valid then we generate brand new form and rendr template
    -we get validation erros and any prevoiusly entered data would also be saved and would have been pre populated into that form
    -we might want to overwrite predefined behaviours.
    -required removed this from page source and it will give unordered list
     

Customizing the form controls:
    -we can configured form behaviour and how this form is rendered and label is showing up here
    -we ca add couple of keyword args that allow us to configure
        label: capitalize first word and replace _ with white space -> label="YOur Name"
        max_length=10 : check html attribute.  
            try removing mannually . it is being validated on server.
        error_messages={} key are the validator identifiers (django knows) 
            values are the error messages
            by default -> "required" validator 
            by default attributr required=True 
        can set required=False to allow empty field
    -html inspect
        <input type="text" name="user_name" maxlength="10" 
        required="" id="id_user_name" spellcheck="false" data-ms-editor="true">
    
    
Customizing the rendered HTML:
    -customizing what is being rendered where instead of customizing this text.
    -right now we are rendering whole form not the element actually:
        {{form}} 
    -we want to render error below the input field not above
    -instead of render whole form,render individual part of form
        {{form.user_name.label_tag}}
        {{form.user_name}} -> input field
        {{form.user_name.erros}} -> error msgs
    -wrapping into div for styling purposes 
        added class="form-control"
    -we might want to add css class dynamically when input is invalid
        it will return true if it is dictonary with error msg inside
        added error in class
        {{div class="form-control {% if user_name.error %}errors{%endif%}" }}
            inspect both cases: form-control and form-control errors
    -we had to manually remove required max_length in html to render desired output
    
Adding styling:
    -django has built in errorlist clas. i.e. <ul class="errorlist"> ...
        can customize it in forms.py with error_class
    -created static/review/style.css in review folder
    -load static file into review.html 
    -we have to inspec with removing required to see error msgs style

Adding more from controls:
    -adding a review_text field
        controlling which kind of html element is being rendered.
        for charfield it was input element of type text.
        but for feedback text render a textarea instead of charfield so we can add longer text
        add widget parameter to textarea and now inspect
        setting max_length
    -adding a rating field with integerfield,label,min value,max_value
    -   
        review_text=forms.CharField(label='Your feedbsck',widget=forms.Textarea,max_length=200)
        rating=forms.IntegerField(label='Your Rating',min_value=1,max_value=5)
    -if you save and revisit local host 800 you wont find changes. because we have manually rendered the username field
        if we have used {{form}} then everything would be showing up.
        we will rendered mannually because i want to have that wrapping div
    -copy that whole div and change to review_text also change to if check
    -do same for rating.
    -we are manually repeating  which is not convinient way to outputting our forms
        same kind of html code repeat over and over again
        
         <div class="form-control {% if form.user_name.errors %}errors{%endif%}">
        {{ form.user_name.label_tag }}
        {{ form.user_name }}
        {{ form.user_name.errors }} 
        </div>

        <div class="form-control {% if form.review_text.errors %}errors{%endif%}">
            {{ form.review_text.label_tag }}
            {{ form.review_text }}
            {{ form.review_text.errors }} 
        </div>

        <div class="form-control {% if form.rating.errors %}errors{%endif%}">
            {{ form.rating.label_tag }}
            {{ form.rating }}
            {{ form.rating.errors }} 
        </div>

        {{form}}
        
        it would be great if we wont have to repeat this all time
        can do with for tag
    -we want to loop through all the fields of form and then output this div for every field
    -start for tag and copy one div and replace form.user_name with field
        we can outsource this div block into an include at html file, and then just repeat included html snippet
        but here we are  fine
    -now we have very lean template where we go through all the fields in form
    -after input check cleaned_data in terminal
        {'user_name': 'ABHISHEK', 'review_text': 'I AM CERTIFIED BACKEND DEVELOPER', 'rating': 5}
    -visit official docs for other form fields
    
Storing form data in database:
    -for the moment we are just printing input
    -it would be realistic to store in db
    -lets add model
        create a new class Review and extend models.Model here
        add fields
            username from models. not from forms.
            can validate but also validated on form. i.e. max_length=100 . we are validating again
            we can omit the validation but max_length is actually still required to configure db correctly
            review_text field it is here textfield. in form it was chafield with widget 
            added rating field
            model is about how data is stored in db. and form is about fetching data in db
        run makemigrations and migrate
    -now if we have valid data we can create new review by instantiating this review class
        populate with different properties
        and save the instance of review class
        imported models
        instantiating and saving the instant
    -to see data on db server
        use shell
        import model
        Review.objects.all()
        Review.objects.all()[0].user_name #access using indx
Introducing ModelForms:
    -we have noticed model is very similar to form class.
        there are difference regarding arguments
    - if we have form which in the end just require to fetch the user input for some model, 
        then we can also let django create a form based on your model basically like we did it in admin panel.
        not restricted to admin panel but any template
    -creating a review form little bit differently
        extending forms.modelform->still create form object
        now we can connect to model and django wil automatically take all the model fields and give us pre configured form
        letting know django to which model form is related
            by nested meta class used yb django whenever you have class which you want to configured as whole
            ad model property and set equal to which this form should be related
            importing models
            not instantiating just pointing
            you may have fields in models which should not necessarily rendered in template(form)
                i.e. owner_comment not should be exposed to our user
                django want us to explicitly specify 
                add fields field as list
                    __all__ for all fields . otherwise as a list
                    except for the id ,this automatiaclly added id field that will never recieve a form field.
                alternatively can exclude particular field  
        this form is based on modelform
        notice labels 
        even it is inferring automatically we can still configured this form

Configuring the ModelForms:
    -setting our own labels and error msgs
    -can add more settings to meta class 
    -using label(dict)
        key from form and value is user dependent
    -same for error-> error_messages(dict)
        nested dict as value
    -can use different approach of creating form and model and then combining into views
    -being able to infer our form from the model could be useful because it required less work
    -need to inspect and removed required and max_length to see errrors
    -In Django, the required and max_length errors are part of the default field validations 
        that Django performs when processing form submissions
    -coming to view

Saving data with ModelForm:
    -using a modelform ,we can change to code for saving to the db
    -what are we doing in view is  we are populating our form with submitted data 
        and we need to do that  to then validated.but once data is validated we create a model instance and save that and it works
    -if we are using modelform  we can skip that instance step and simply call form and save it
    -because this form is modelform and it will save to db through review model
    -we cant just call save upon new data but also on existing data
        if we have existing review which we want to update then pass extra argument 
            to constructor as instance=..
    -no need to instantiate just call save upon it.       

Class based views:
    -we have always define views as function 
    -instead of definning them as function we can also define them as class
    -transforming review funcion to class
    -add a new class in views.py pick a name
        extend from django.views import View to class
        add methods to this class
        when extending the built in view class ,you add methods that carry name of HTTP methods you want to support
        def get(self,request) and def post(self,request)
        django wioll automatically call appropriate methods
        change to urlpatterns to view.Class_name.as_view()
    -in official django docs click built in class based view
        for fetching database ListView
        DetailView->
        Form view->
Summary:
    -

11 Class based views:

Module introduction:
    -closer llok at the class based views
    -inherited from view class in last lec.
    -we will take a look at 
        template views
        list and details views
        form view and create/delete/update view

Adding templates:
    -creating a base.html. we can also setup a route templates folder in the overall project
    -not adding any css files, we will go with existing css files
        added link and loaded static in base.html
    -extended base.html to review.html and thankyou.html
    -now we will add more url
    -individual review to dive in
    
        
Templateview:
    -rendering thankyou template with basic function
    -converting thankyou to class based view
    -created THnakyouView class and extend that to view class
        setted get method. has no post method because no post method will reach this view
        return a response in get method
        change urlpattern of views.thank_you
    - if we have view which primarily deals with showing some template  then inherit from view
    -but we can also use specifcally geared for returning a template
        add  from django.views.generic.base import TemplateVIew
        extend just like view
        it is more specific and its allowing you to build a view classes that render a template
    -defining templateview doesnot require get method, what we need to do is,
        set template_name='route/template.html'
    -we might have template where you want to add some extra context
        for passing context ->def get_context_data
        the idea here is that in this context data, in get context data method, you should return the context that is exposed to the template 
        so that dict of key value pair, which should be exposaed to this template 
        ypu should also call super get context data here but you dont necessarily need to return a result of that
        dont forge to add interpolation syntax in html page
        
    get_context_data Method:

        This method is overridden to provide additional context data to be passed to the template.

        The super().get_context_data(**kwargs) line calls the same method in the parent class (TemplateView) to get the default context dictionary.

        In your case, the line context['msg'] = 'this is context!' adds a key-value pair to the context dictionary. This means that when the template is rendered, it will have access to a variable named msg with the value 'this is context!'.

        Finally, the method returns the updated context dictionary.
    
        

Using the templateview:
    - -lets use templateview to output a list of all the reviews we received thus far.
    -adding a new template here review_list.html
        extends to base html
        title block
        content block
            use for tag to render all reviews
        we need to add a new view
    -class ReviewsListView inherit from template view/ can also inherit from view
        setting template_name
        get context data method
            getting context from parent class 
        we also need all reviews so importing models and assigning it to attribute reviews
        now add a key to context 
        our model review is made up of username reviewtext and rating
            lets output username  and rating and make that a clickable link which then takes us to detail page
            that will be step num 2. step num 1 is output that list
        make sure that this is also loaded for specific url 
        add a new path
        data will be coming from db     
    -we will also build detail page where we see single review and where we then also have a review text

Showing a detail template:
    -building a detailed view
    -add a single_review.html template
        idea is here to output username reviewtext and rating 
    -add a view for this
        class singlereviewview and inherit from template view
        template_name....
        def get context data....
    -add a new path for this view
        this will be reviews/<int:id>(id of that review) id will number so add int path transformer in front of it to convert this to a number
    -in views.py we want to load that single review
        context get kwards argument
        through kwargs we can  get access to this dynamic segment 
            add review_id =kwargs['id']  because we have used id as identifier in path
            now through review id we have selected review id
            and pass selected review id as context
    -apply interpolation syntax to and output review.user_name and so on..
    
The listview:
    -we have uses classes based on templateview and such type of cases are so common
        outputting a list of data
    -django has specific view classes for these scenario 
    -starting with reviewlistview class
    -whenever we have template and we want to output a list of data
        django.views.generic import listview   
            its still all about rendering a tempelate for a get request but it then also specifically for fetching 
            list of data based on model
            so exxactly what we doing till here
        inherit from listview
        get rid of get context data 
        add model property(from which model django should fetch data)
            not instantiating just pointing at.
            can override num of methods i.e. def  get...
    -by default django will fetch data related to model and pass it to template
    -if reload it will failed. why ? because django will fetch us data not in reviews as before but as object_list
        so change to object_list in html in for loop
        we can change object_list nomenclature how? built in feature
        add context_object_name property set i9t to reviews 
    -if we want review which  has rating >4
        override get query set method it will return a query set and use all query methods like learned earlier
    -#store in new variable and return it

The detailview:
    -detail view for simplyfying view
    -whenver you in the end have the goal of returning a template for a get request with data about a single piece 
    of data using the detail view instead of template view with your own logic could be worthwhile to consider
    -import detailview
    -in singlereview view inherit from detailview
        aware detailview from model
        set model property and template property
        fetching a single piece of data based on that model does not require context 
        how will django identify single item? -> slug or PK how? define in your url
            change this id to pk -> value enter here should be treated as PK by which django will find single piece of data
            (model has default id field. adding pk will make django to look out primary key field in django)
        in html page, django will automatically take model name in lowercase for template i.e.{{review.user_name}}
        alternatively we can use object. i.e.{{object.user_name}}        

When to use which view:
    -when we have page like thankyou when we dont have to involve database->templateview
    -if we want to support both get and post methods and you want to then write the code that should execute 
        for those different methods very explicitly->basic view 
    -what if we have form and data is being submitting?

Formview:
    -Specialized in form handling
    -in general scenario,
        support get request to display form ,support post request and also handle form submission and possibly 
        validate form errors.
        flow will remain same most of the time. 
    -change in reviewview 
        From Formview django.generic.edit import formview
        extends to formview
        changing logic:
             add form_class property which lets django know which form class should be used
             also letting know what iur template file is. which template should be use for rendering the form
             add template_name
             django will automatically replace get method 
             for form submmision?->django will handle this 
             try submitting in invalid way
                removed required->automatically get error
            if you try to submit it will show success_url error
            we need to let django where it should redirect to when the form is successfully submitted
            give success_url='/thank-you'
    -if you visit reviews you will find last added entry is missing because formview doesnt know what to do with submitted data
        maybe we wanna write it to file or send mail or print to console
        so need to extra method-> form_valid
            executed by django when form is submitted when valid form is submitted
            must return super form_valid here
            we only receive form when it is valid so we have to just save it->form.save()
            remeber you have filter there. give rating 5
                
Create view:
    - we can get even more specific than with the formview
    -there are even more specialized views which we can utilized
    -import create view from .edit 
        more specialized then formview
        automatically save data for us,create data
    -inherit from CreateView to ReviewView
        no need to specify form class here
        dont even need to create a form class
        set a model again because its need to know from which model data should be generated
        so in this Review model ->automatically infer model form based on that model
        add fields -> fields='__all__'
        alternatively can set form_class='ReviewForm which is model form
        in formview we configure labels and error msgs which is not possible in createview
        here we will let creteview know the which model this all about and which form class to use
        we can get rid of valid data here 
        after submitting form look at reviews
        only give /thank-you not  reviews/thank_you.html
    - we also have updateview and deleteview
        they basically works with fetching data and present a form with prepopulated data
        and updating that data in db once the form is submitted
    -deleteview to deletedata

11 Forms:

starting setup:
    -created a new app named profile and copied all sub folders fom site
    -add profiles to installed app otherwise template wont be picked up.
    -added profile app so need to add its url to project url i.e. path('profiles')
    -also add url in profile app for profile/
    
making the file upload work:
    -we have form which has input type file and upload button in  create profile html\
    -class of profilview for handling this form
    -setting action attribute in form at /profiles and method is post
    -for file upload we have to mention enctype
        this tells the browser that this form when submitted will contain a file,
        and tht will simply changehow the req is sent to server.
        properly configured req is sent to server specifically it will be
        post req sent to /profies
    -in post def
        request.post gives us accesss to alll submitted form data 
        request.FILES-> file data->access to uploaded files
        add name to input type i.e. image
        request.FILES['images']
         print('->',request.FILES["image"]) #we get complete name here. its not just name but completeobject which we can work with
        for the moment we are printig to get idea and redirect ing again at /profiles
        add slash at the end in profiles.  i.e. form action='/profiles/'
        add csr token(position is imp bcoz didnt worked for at the end or beginning)
        dont do mistake in post method of form in typo
    -search for uploaded files and upload handlers. property and methods which we can access
        name size contenttype
    -we are not seeeing any file now but in reality we might want to store such files.
    
    
storing uploaded file naive approach properties:
    -now we want to store it
    -adding a helper fn . we could create a diffnt file as well but i want to keep it here so we can see it here
        store_file fn responsible for storing file in our sys
            file handling
        we have assumption that it will only work with jpg file.adjust appropriate extension
        calling chunk->uploadedfile.chunks(chunks_size=)
        can use read but if large file go for chunks. know diffnce
        we will write chunk by chunk in dest
        we have given temp/... so need to create folder not in profile but at global project level
        this approach has couple of flaws 
            static -> works only with file.extension extension
            we have custom logic which is not flexible 
        we will dive into varoius functionality offered by django by us to managing to file uploads
adding a form with filefield:
    -here file input is just form input
    -why dont we handle it with oreign tools?
    -adding a new forms.py in profiles
        creating a form which will be based on django's form functionality which hopefully
        simoplifiles  file uploading task
        import form 
        create profile class and ingerit from forms.form
        adding only 1 field user_image which is filefield
            allowed empty file attribute
    -now we want create such form 
        import forms in views.py
        create a form by instantitaing profileform class
        and pass context wich is form object
    -in templates replace all the inputs with forms 
        we have full control over errors,labels,controls.
    -still handling upload logic mannually in post method
    -we can also create a profileform there though to pass into submitted data also to submitted files
        profileform(request.post,request.files) which is out submiited_form
        checking is valid?
        if yes then store the file and dont then return create_profile.htyml
    -uploading empty files genrates browser error
    -try to cheat by removing required, you will get this field reqquired error as ol
    -here its no help when it comes to storing the file. to simplufy that we wanna combined a form with model
        because it turns out that all uploaded files is related to model
        i.e. image of user is related to user model
    
    -
    """
    GET Request:
        When a user initially accesses the page (via a GET request), 
        you want to display the form.
        In your get method, you create an instance of the ProfileForm 
        and pass it to the template so that you can render the form fields in your HTML template using {{ form }}.
        
    POST Request:
        When the user submits the form (via a POST request),
        you create another instance of the ProfileForm,
        this time passing both request.POST and request.
        FILES to handle form data, including file uploads.
        You then check if the submitted form is valid using is_valid().
        If the form is valid, you can proceed with processing the data (in your case, calling storing_file to handle the uploaded file) 
        and redirecting the user.
        If the form is not valid,
        you need to render the form again in the template
        to show error messages and allow the user to correct their input. 
        This is why you set context['form'] to the submitted form instance."""

using models for file storage:
    -adding a new model userprofile and extends 
        here more data could be added but we have file image only 
        starting with imagefield
            the filefield wants a file but the interesting thing now is that this file
            will not be stored in database because it is considered a bad practice to store file in db.
            files should be stored on hard drives
            ff will take that file and move it somewhere and only sore the path to that file in model(db).
            it also handles moving that file to that location for us.
            so we dont need to mannually need to move  to the file anywhere
            add upload_to parameter
                we dont want to construct a long path which would have to be absolute on our entire file sys.
                if we add 'data' then it will look for a data folder on the root level of our os
                go to feedback-> settings.py->add a new setting
                    MEDIA_ROOT
                        it will tell django where our files should be store in general.
                        then any folders we might point at in our models will be sub folder to that media_root.
                        media root should be absolute path
                        to construct path we use base_dir  and thenn simply adds 'uploads'
                now uploaded files will be stored in 'images'
    -now we have this profile and using this model in views.py
        instead of storing file like storing_file(....) we can create our profile,
        we can instantiate our userprofile model and then set imagefield by adding image argument
        identufier here is user_image because our form is rendered with the help of {{form}}.
        now behind the scene, it will take the file, move it to some location and only store a path
    -saving form.save() will negate the use of helper function
    -dont forget migrations which is neccessary to intialize db
    -after operation check uploads folder
        if we run w/o migrations then file will store if we had name clash then django will automically assigned diffnt name 
    -to see path in db
        shell
        import userprofile ->from profiles.models import UserProfile
        objects.all() ->:<QuerySet [<UserProfile: UserProfile object (1)>, <UserProfile: UserProfile object (2)>]>
        objects.all()[0].image -><FieldFile: images/sunflower1.jpg>
        objcts.all()[0].image.path  ->'C:\\Django_projects\\feedback\\uploads\\images\\sunflower1.jpg'
        objects.all()[0].image.size ->169137
    -utilize a model that let django take care of upoloaded file
    -profile=UserProfile(image=request.FILES['user_image']) made a mistake with request.POST
         
using an imagefields:
    -here we are using filefield even though we are interested in images.
    -imagefield. idea is still same. move to the folder.
    -change filefield to imagefield and django will only accept images
    -if we run our development server it will display some error
        -m pip install Pillow".
        some missing packages errors
    -dealing with images spevifically,and for analyzing images and files we need to install extra package.
    -once it is done rstrt devlpment server
    -also switch imagefield to form 
    -inspect html
        accept="image/*"
        we have browser validation and it will also validate on server.
    -uploading document other then image will cause this error
        User image:
            Upload a valid image. The file you uploaded was 
            either not an image or a corrupted image.

using a createview:
    -we have model and form we can create modelform
    -if we dont need any special configuration regarding labels and error messages,
        we can go for createview 
    -create a view and extends to createview class
        we dont need to add get and post method so on.
        inform django about our template
        about model
        all the fields should be rendered (tell django) in the template
        add succes_url
        validation and saving the data including files taken care by django
        getting rid of old createprofileview.
        we dont worry about nitty gritty details
        we can delete form class. all we need is model
        serving this file functionality is missing.  
            
working with the field:
    -create a new template user_profile.html
    -goal is to output ul of all user profiles.
    -now we need a view which fetches all images and exposed to template
    -create a new class profileview and extends to listview
    -add a model
    -add a template_name
    -define success_url
    -define context_object_name 
    -register inn urlpatterns
    -loop through all profile in rendered temp
        if it were static file then <img src="{% static.. %}"
        {{profile}} is instance and we have image field so {{profile.image}}
        its a kind of static ,its an image, its not template not python code,
        but its not also one of our predefined static files.
        all those files managed by our models ,brew the imagefield or filefield.
        now on that image we can drill into things like path or url
        path would be wrong because thats a file sys path, which is nice to have,
        if we run some python code on our server.
        remeber we are definnig img src so that browser can reach and .path is not accessible by browser
        {{profile.image.url}}
    -django gives us a URL field on the files stored through a file field or
        image field in our model.
    -if we run our dev server we will get destroyed img instead some placeholders
        it does have url here but fails to fetch them
        GET /images/sunflower1_f321QOh.jpg HTTP/1.1" 404 2903
serving upload files:
    -why is django not able to find our images 
    -by default django locks down all your folders and does not expose them to browser for security reasons.
    -the static files like css are exposed by django.
    -in general nothing is accessible.
    - now we have to do 2 things.
    -go to settings
        add media_url='//user-media'
        it will be part of the url which will be exposed to outside the world,
        for accessing your uploaded files.
        django also does similar for static files i.e static_url 
    -this alone does not exposae anything
    -go to global url.py->(not sure) but experimenting on static in profiles
        import static and call static fn  which is helper fun which servers static files.
        django autmotically configured  to serve css files in develoipment and static images.
    -static wants 2 args.
        it wants to know url which should be used for exposing the files 
        and then path on our file sys that hold actual files
        media_root= path where files are physically sotred
        media_url= url we wanna outside the world
        and mapping between them done by static fn
        django will automatically pickup url and add it to image.url in html
        do it on global url.py not app speciic
            because it is this main entry point  for all req where
            you need to enable this static serving off your user uploaded data.         
summary:
    -
13 Sessions:

Module intro:
    -sessions can be defined as temporary persitent data

Problem Description:
    -i would like to have  favorite button below my reviews so on the single review page .
    -when i click then this review should become my fav. and if i have existing fav then it should be replaced.
    -if we have multiple visitor every visitor have his own fav.
    -i dont want edit review data in db, review model and mark this as fav. instead it should be user specific data.
    -that where sessions are able to help us,we will be able to store user specific data,without directly interacting with the db.
    
What are sessions:
    -A ongoing conn betn a client(browser) and server.
    -ongoing also means that its persist and lives on even if browser is closed in between even if comp is shut down.
    -it can be deleted cleared and reset. so its not forever  but it is long livnig. how long will session survive will be in hands of developer.
    -sessions are about storing data.
    -data stored in a session persists as long as the sessions is active.
    -in admin panel we logged in thorugh superuser. the info in admin panel  after loggin are stored in session which has,
        the effect  that if we reload browser page we dont hve to login again.
        w/o session we have to login again whenver we close the browser or reload the page.
        indirectly using session.
    -the django running on server stores the sessions data and a unique session identifier,
        because multiple users of same website will have multiple session.
    -client stores a coockie which sent by server which contains that session identifier,
        so with that client is able in future for future req to send that coockie to server.
        the server can lookup that sessions in db and send that session specific data back to cllient
        i.e if sessions contains logged in data then server may grant access to protected resources.
        django will already create a cookie and send that cookie to the client
        django will store the session in db.
    -we as a developer just needs to configure how sessions should behave 
    
Enabling and configuring sessions:
    -to enable sessions we first need to dive into settings.py
    - make sure that sessionmiddleware is added in middleware list
        django.contrib.session must be part of installed apps
    -in the bottom add session_coockie_age
        here we can define how long a session cookie and therefore the session itself should survive
        default is 2 weeks but can set and must be in seconds
    -we are fine with default of 2 weeks
Adding a new view:
    -we want to make sure that whenever fav button in single_review.html is clicked,
        we send a req to dj to our server and there we trigger some logic in some view,
        which will allow us to set this req as our fav review 
    -to send req wrapped button inside form
        right now there is button inside form , and isnt any data attached.
        so adding input type hidden
            thats the input which the user cant edit but which will still submitted as the req body.
            <input type='hidden' name='review_id' value={{review.id}}>
    -so the id of the to be fav review is part of post req 
    -set up url for that.
    -adding before <int:id> because i dont want fav to be interpreted as a pk. so i am,
        doubling down that and i want to be super safe by making sure that this path is ,
        evaluated first before djago consider sending my req off.
    -setting view for logic implementaion.
        get the review id and marked as favorite
        we can get full object of review model based on that review_id
Storing a data in sessions:
    -request object has by default session property.
    -add a new data by adding a key and value. -> req.se['fav_review]=fav_review
    -so the favreview , review obj gets stored in my session with the key.
        under the hood dj will make sure that this data is then stored to the db
        along with all our session data that belongs to me and that data will always be accessible,
        if i send req to server 
    -sending user back to review detail page 
        can use reverse fn instead of httpresponseredirect
    -missed csrf token because we got form here. 
    -visit reviews/1 or 2 or 3
    -error: object of type review  is not json serializable
        session and serializabilty in next lec.       
which kind of data should be stored:
    -the problem is we are storing review object
    -under the hood django takes whatever we store in a session and serialize it to format called json.
        popular data format in web development.
    -the problem is that objects cant be serialized to that because they dont just contain data,
        but they can also contain methods and those cant be translated to json.
        thats why we cant store an obj like this
    -so store primitive values like strings in sessions.
    -so storing just review_id in our session.
    -we are alreasdy fetching the full review object (singlereviewview class).
    -so change to fav_review to review_id to session
    -lets utilize this session and also read from that session.
    -after adding to fav it will redirect to same page
    
Using session data:
    -reading data from session,storing data wont be helpful.
    -reading from singlereviewview.
    -also find out whether review which are loaded is fav or not.
    -access the session?
        override get_context_data method of singlereviewview
        this method defines the context that will be set for template 
        this will for example contain the single review which had fetch automatically.
        because thats the idea behnd detailview.
        so that will be part of that context and storing it.
        adding more data to context
    -fav rev key is equal to review_id -> logic
    -we can get access to the loaded review through self.object
        will give us access to automatically loaded review.
    -accessing req through self.req
    -if fav id is there then output paragraph else review.
    - def get_context_data(self, **kwargs: Any):
        context=super().get_context_data(**kwargs)
        loaded_review=self.object
        request=self.request
        favorite_id=request.session['fav_review']
        context['is_fav']=favorite_id == loaded_review.id
        return context
        #the value which should be stored in the context uneder is_favorite key,
        #should be then result of the comparison where i compare the fav_id from my session to the id of the loaded review like this.   
    - if you hit enter on fav that doesnt seem to work because yo will redirect on same page
    -its related to which data we are storing in session.
    -here we are storing review_id. Which type of data though? its number or string.
        its actually coming from this form from this input.
        and such data always treated as string.so we had store id as text in session.
        however loaded id field will be a integer.
        so this comparision doesnt yield true.
        converting loaded_review.id as string.
        
Safely accessing session data:
    -we might face error such as keyerror 'favorite_review'.
    -trying to access fav review on the session can fail if itwasnt set before.
    -so the safe method is use get
    -favorite_id=request.session.get('fav_review') 
        #safer way to access data is using get method.
        because this will not throw an error if fav review doesnt exist yet.
    
summary:
'''
