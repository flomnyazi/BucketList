function check(form)/* checks if username and id are matching*/
{
  if (form.emailid.value=="myemailid"&&form.pswrd.value=="mypswrd")
  {
    window.open('bucketlist.html');
  }
  else
  {
    alert ("Oops! Incorrect Username or Password");

  }
}
<form class="form-horizontal" role="form" method="post" action="#">
<button type="submit" class="btn btn-primary" id="register">LogIn</button>
