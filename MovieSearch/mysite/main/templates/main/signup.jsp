<html>

<head>
  <title>회원가입</title>
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css" integrity="sha384-UHRtZLI+pbxtHCWp1t77Bi1L4ZtiqrqD80Kn4Z8NTSRyMA2Fd33n5dQ8lWUE00s/" crossorigin="anonymous">
<link href="https://fonts.googleapis.com/css?family=Baloo+Paaji&display=swap" rel="stylesheet">


  <!-- jQuery !-->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.js"></script>
  <!-- Bootstrap !-->
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

  <style>
    body {
      background: black;

    }

    #searchbar {
      text-align: center;
      color: white;
      margin-top: 40px;
    }

    #nav {
      height: 80px;
      color: #960303;
      border-bottom: 2px solid #3a0707;
	font-family: 'Baloo Paaji', cursive;
    }

    .logo {
      padding: 5px;
      margin-left: 15px;
      float: left;
    }

    .menu {
      float: right;
      list-style: none;
      margin-left: 2%;
      padding: 15px;
      font-size: 23px;
    }

    a {
      color: #960303;
      text-decoration: none;
      outline: none
    }

    .signup {
      padding: 50px;
      color: white;
      width: 500px;
    }

    h2 {
      text-align: center;
    }
  </style>



</head>

<body>
  <!-- jquery cdn -->
  <script src="https://code.jquery.com/jquery-3.4.1.js" integrity="sha256-WpOohJOqMqqyKL9FccASB9O0KwACQJpFTUBLTYOVvVU=" crossorigin="anonymous"></script>
  <!-- Bootstrap cdn !-->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

  <div id="nav">
    <h1 class="logo"><a href="https://moviesearch-sncjv.run.goorm.io">Search</a></h1>
    <!-- 헤더공백  -->
    <nav>
      <ul>
        {% if user.is_active %}
        <li class="menu"><a href="https://moviesearch-sncjv.run.goorm.io/signup">Signup</a></li>
        {%else%} <li class="menu"><a href="https://moviesearch-sncjv.run.goorm.io/login">Login</a></li>
        {%endif%}
      </ul>

    </nav>
  </div>



  <!-- 회원가입폼 -->
  <div class="container signup mx-auto mt-5">
    <h2>
      signup
    </h2>

    <form action="" method="post" class="form-signup">{%csrf_token%}
      Username:
      <br>
      <input name="username" class="form-control" type="text" placeholder="username" required="required">
      <br>
      Password:
      <br>
      <input name="password" class="form-control" type="password" placeholder="password" required="required">
      <br>
      E-mail:
      <br>
      <input name="email" class="form-control" type="email" placeholder="email" required="required">
      <br>
      UserComment:
      <br>
      <input name="user_comment" class="form-control" type="text" placeholder="user_comment" required="required">
      <br>
      Selected:
      <br>
      <input name="selected1" class="form-control" type="text" placeholder="selected1" id="selected1" style="height:30px;" readonly>
      <input name="selected2" class="form-control" type="text" placeholder="selected2" id="selected2" style="height:30px;" readonly>
      <input name="selected3" class="form-control" type="text" placeholder="selected3" id="selected3" style="height:30px;" readonly>
      <input name="selected4" class="form-control" type="text" placeholder="selected4" id="selected4" style="height:30px;" readonly>
      <input name="selected5" class="form-control" type="text" placeholder="selected5" id="selected5" style="height:30px;" readonly>
      <br>
      <button class="btn btn-dark btn-block btn-large" >Signup</button>
    </form>

  </div>

</body>

</html>


  <script>
      temp = decodeURI(location.href).split("?");
      console.log(decodeURI(location.href));
      temp2 = temp[1].split("=");
      temp3 = temp2[1].split(",");
      var temp4=[];
      for(i=0;i<temp3.length;i++){
          temp4[i] = temp3[i].substr(5,temp3[i].length-7);
          document.getElementById('selected'+(i+1)).value += temp4[i]+"\n";
      }
  </script>


