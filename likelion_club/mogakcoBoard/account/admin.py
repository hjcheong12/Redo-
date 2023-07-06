from django.contrib import admin

# Register your models here.

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            width: 60%;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        a {
            text-decoration: none;
            color: #000;
            outline: none;
        }

        .header{
            width: 100%;
            text-align: center;
            padding: 10px 0px;
            background-color: aliceblue;
        }
        .container {
            display: flex;
            flex-direction: column;
            align-items: stretch;
            width: 100%;
        }
    </style>
    <title>LikeLion11th</title>
</head>
<body>
<div class="header">
    <h1>멋사대학교 동아리를 소개합니다</h1>
</div>

<div class="container">


    {% block content %}
    {% endblock %}

</div>
</body>
</html>