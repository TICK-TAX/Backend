<!DOCTYPE html>
<html lang="en" dir="ltr">
  
  <head>
    <title>Index</title>
    <meta charset="utf-8">
    
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/stylesdet.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/stylebody.css') }}">
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/js/bootstrap.bundle.min.js"></script>
    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <style>
      button:hover{
         background-color: #FFFFFF;
         color: #1e2833;
         text-decoration: underline;
       }
      button.first{
        background-color: #1e2833;
       }
      button.first:hover{
        background-color: #000000;
        text-decoration: underline;
       }
   </style>
    
  </head>
  
  
  <body>
   
    <div class="upper-logo">
      <img src="/static/image/logo3.png" alt="pic1">
    </div>
   
    <div class="float-container">

        <div class="float-child-left left-logo">
          <img src="/static/image/logo2.png" alt="pic1">
        </div>

        <div class="float-child-right">
          <div class="container" id="container">
            <div class="form-container sign-up-container">
                <form class="#" action="index.html" method="post">
                  <h1>Create Account</h1>
                  <div class="social-container">
                    <a href="#" class="fa fa-facebook"></a>
                    <a href="#" class="fa fa-google"></a>
                    <a href="#" class="fa fa-twitter"></a>
                  </div>
                  <span>or use your email for registration</span>
                  <input type="text" placeholder="Name" />
                 <input type="email" placeholder="Email" />
                 <input type="password" placeholder="Password" />
                  <button class="first">
                    <a href="home.html" style="color: #FFFFFF">Sign Up</a>
                  </button>
                </form>
            </div>

            <div class="form-container sign-in-container">
             <form action="#">
               <h1>Log In</h1>
               <div class="social-container">
                  <a href="#" class="fa fa-facebook"></a>
                  <a href="#" class="fa fa-google"></a>
                  <a href="#" class="fa fa-twitter"></a>
               </div>
               <span>or use your account</span>
               <input type="email" placeholder="Email" />
               <input type="password" placeholder="Password" />
               <a href="#">Forgot your password?</a>
                <button class="first">
                  <a href="home.html" style="color: #FFFFFF">Log In</a>
                </button>
             </form>
           </div>

            <div class="overlay-container">
             <div class="overlay">
               <div class="overlay-panel overlay-left">
                 <h1>Welcome Back!</h1>
                 <p>Already a member? Just log in and do your payments efficiently!</p>
                 <button class="ghost" id="signIn">Log In</button>
               </div>
               <div class="overlay-panel overlay-right">
                 <h1>Hello There!</h1>
                 <p>New to us? Join now to make your life a lot easier!</p>
                 <button class="ghost" id="signUp">Sign Up</button>
               </div>
             </div>
           </div>

          </div>
        </div>

   </div>
    
    <script type="text/javascript">
      
      const signUpButton = document.getElementById('signUp');
      const signInButton = document.getElementById('signIn');
      const container = document.getElementById('container');

      signUpButton.addEventListener('click', () => {
         container.classList.add("right-panel-active");
      });

      signInButton.addEventListener('click', () => {
         container.classList.remove("right-panel-active");
       });
      
    </script>

  </body>
</html>
