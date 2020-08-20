## Service Name
Moive Search

## Project Introduction
This service is a website that provides recommended movies based on the genre that users prefer.   
IMDB's movie rating(review) dataset is used, and movies with high ratings are preferentially recommended   
based on the genre that users prefer.

### why we developed?
We decided to create a movie recommendation website for us who love both movies and programming.   
It was developed with an emphasis on data processing into useful information using big data (IMDB's movie dataset).   

### Period   
Duration : 2019.9 ~ 2019.12   
Technologies used : HTML5/CSS3, JavaScript, Python, Djagno, SQLite, Image Search API   
Role : 
Frontend - Movie Poster Printing function, Search function, movie_info.csv file Data/String Processing(Ajax),    
           User preferred genre priority printing function    
Backend - Image Search API(Bing Image Search), IMDB Movie Dataset Processing(Voterate sorting), AbstractUser Design(models),  


### 활용한 라이브러리 및 프레임워크
Django, Bing Image Search API

## 설계
|기능 요구사항|구조|프로세스|
|---|---|---|
|![유스케이스 다이어그램](https://user-images.githubusercontent.com/55237012/90137017-fc4ad780-ddaf-11ea-8f01-147425f7f164.png)|![클래스 다이어그램](https://user-images.githubusercontent.com/55237012/90137020-fd7c0480-ddaf-11ea-8f24-53c2b1a66235.png)|![시퀀스 다이어그램](https://user-images.githubusercontent.com/55237012/90137023-fe149b00-ddaf-11ea-9f08-3d0463b08a95.png)|

### 설계 방법
Model, View, Controller(Template) 패턴을 활용하여 설계하였다.
|Model|View|
|---|---|
|![Model](https://user-images.githubusercontent.com/55237012/90224399-8f385000-de4a-11ea-8389-7fb4bebb9be4.PNG)|![View](https://user-images.githubusercontent.com/55237012/90224437-9f502f80-de4a-11ea-9972-a8b141ff1552.PNG)|

|Template1|Template2|
|---|---|
|![Template](https://user-images.githubusercontent.com/55237012/90224366-80ea3400-de4a-11ea-9bc7-9eada50d4162.PNG)|![Template2](https://user-images.githubusercontent.com/55237012/90224455-aa0ac480-de4a-11ea-93eb-3ac9ac68b56c.PNG)|



## 스크린샷
### 인트로 페이지
<img src="https://user-images.githubusercontent.com/55237012/90220924-20f08f00-de44-11ea-9afd-34536e6ac6c4.png" width="70%">

### 메인 페이지
<img src="https://user-images.githubusercontent.com/55237012/73512006-492a1a80-442b-11ea-934f-109f24a14442.PNG" width="70%">

### 디테일 페이지
<img src="https://user-images.githubusercontent.com/55237012/90220917-1cc47180-de44-11ea-9c87-cb95e35768d9.png" width="70%">

### 게시판
<img src="https://user-images.githubusercontent.com/55237012/90220916-1b934480-de44-11ea-8f42-ef106cde4ea6.png" width="70%">
<img src="https://user-images.githubusercontent.com/55237012/90220917-1cc47180-de44-11ea-9c87-cb95e35768d9.png" width="70%">

## 구현된 기능
<img src="https://user-images.githubusercontent.com/55237012/90137290-6a8f9a00-ddb0-11ea-9449-83984ea540ad.PNG" width="70%">
