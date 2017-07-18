function check(form)/* checks if username and password are matching*/
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
