from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from .models import Html_file
from .models import User
from .forms import UploadFileForm

# Create your views here.

def reg(request):
    if request.method == "POST":    #값을 받을경우 실행
        if request.POST['name'] != "" and request.POST['id'] != "" and request.POST['pw'] != "" and request.POST['re_pw'] != "":
            if request.POST['pw'] == request.POST['re_pw']: #비밀번호가 같을경우
                if len(User.objects.filter(User_id=request.POST['id'])) == 0:   #존재하는 아이디일경우
                    User_qs = User(User_id=request.POST['id'],
                                   User_pw=request.POST['pw'],
                                   User_name=request.POST['name'])
                    User_qs.save()
                    return HttpResponseRedirect(reverse('project:login'))
                else:
                    context = {"mes": "존재하는 아이디입니다."}
                    return render(request, "page/reg.html", context)
            else:
                context = {"mes": "아이디 혹은 비밀번호가 일치하지 않습니다."}
                return render(request, "page/reg.html", context)
        else:
            context = {"mes": "빈칸이 있습니다."}
            return render(request, "page/reg.html", context)
    else:
        return render(request, 'page/reg.html')


def login(request):
    try:
        del request.session['User_id']
    except KeyError:
        pass

    if request.method == "POST":
        post_id = request.POST['id']
        post_pw = request.POST['pw']

        if post_id != "" and post_pw != "":
            if len(User.objects.filter(User_id=post_id)) != 0:
                if post_id == get_object_or_404(User, User_id=post_id).User_id and \
                        post_pw == get_object_or_404(User, User_id=post_id).User_pw:
                    #세션 전달
                    User_qs = get_object_or_404(User, User_id=post_id)
                    request.session['User_id'] = User_qs.id
                    return HttpResponseRedirect(reverse('project:home', args=[User_qs.id]))
                else:
                    return render(request, 'page/login.html', {'mes': '아이디 혹은 비밀번호가 일치하지 않습니다.'})
            else:
                return render(request, "page/login.html", {"mes": "계정이 존재하지 않습니다."})
        else:
            return render(request, "page/login.html", {"mes": "빈칸이 있습니다."})

    elif request.method == "GET":
        return render(request, 'page/login.html')


def home(request, User_id):
    try:
        if request.session['User_id'] == User_id:
            pass
    except KeyError:
        context = {"mes": "로그인해주세요"}
        return render(request, "page/login.html", context)

    if request.session['User_id'] != User_id:
        #세션값이 불일치 할 때
        context = {"mes": "로그인해주세요"}
        return render(request, "page/login.html", context)

    User_qs = get_object_or_404(User, id=User_id)

    if request.method == "POST":
        print("post받음")
        if request.POST['file'][request.POST['file'].find("html"):] != "html":
            context = {"mes": "html파일이 아닙니다.",
                       "User": User_qs}
            return render(request, "page/home.html", context)
        else:   #html파일 받은경우
                    return HttpResponseRedirect(reverse('project:show_html'))

    elif request.method == "GET":
        print("get받음")
        context = {"User": User_qs}
        return render(request, "page/home.html", context)


def show_html(request):
    context = {"mes": "html 변환이 완료되었습니다.",
               "html_file": """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta http-equiv="Content-Style-Type" content="text/css" />
<meta name="generator" content="Blogger" />


<link rel="canonical" href="http://mwultong.blogspot.com/2006/12/html-javascript-print-string.html" />
<link rel="alternate" type="application/rss+xml" title="mwultong Blog ... 디카 / IT" href="https://feeds.feedburner.com/mwultong" />
<link rel="service.post" type="application/atom+xml" title="mwultong Blog ... 디카 / IT" href="https://www.blogger.com/feeds/19884063/posts/default" />
<link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://www.blogger.com/rsd.g?blogID=19884063" />
<style type="text/css">
@import url("https://www.blogger.com/css/blog_controls.css");
@import url("https://www.blogger.com/dyn-css/authorization.css?blogID=19884063");
</style>






  <title>자바스크립트] 문자열 출력 함수, 텍스트 쓰기; HTML-JavaScript Print String</title>



<meta http-equiv="imagetoolbar" content="no" />
<link rel="shortcut icon" type="image/x-icon" href="http://mwultong.googlepages.com/mwultong.ico" />

<!-- http://mwultong.blogspot.com/ -->

  <style type="text/css">


	/* Primary layout */

body	{
	margin: 0;
	padding: 0;
	border: 0;
	color: #554;
	background: #692 url('https://photos1.blogger.com/blogger/2921/1916/1600/outerwrap.gif') top center repeat-y;
	font-family:Tahoma, Dotum, 'Bitstream Vera Sans', 'Trebuchet MS', 'Lucida Grande', lucida, helvetica, sans-serif;
	font-size:10pt;
	}

img {
	border:0;
	display:block; }


	/* Wrapper */

#wrapper	{
	margin:0 auto;
	padding:0;
	border:0;
	width:693px;
	text-align:left;
	background:#FFFFFF url('https://photos1.blogger.com/blogger/2921/1916/1600/innerwrap.gif') top right repeat-y;
	font-size:90%;
	}


	/* Header */

#blog-header	{
	color:#FFFFFF;
	margin:0 auto;
	padding:0 0 15px 0;
	background:#88BB22;
	border:0;
	background-image:url(https://photos1.blogger.com/blogger/2921/1916/1600/headline_brush_wineglass.jpg);
	background-repeat:no-repeat;
	background-position:bottom right;
	}

#blog-header .myh1	{
	font-size:24px;
	text-align:left;
	padding:18px 20px 0 20px;
	margin:0;
	}

#blog-header p	{
	font-size: 110%;
	text-align: left;
	padding: 3px 20px 10px 20px;
	margin: 0;
	line-height:140%;
	}


	/* Inner layout */

#content	{
	padding: 0 20px;
	}

#main	{
	width: 400px;
	float: left;
	}

#sidebar	{
	width: 226px;
  float: right;
	}

	/* Bottom layout */


#footer	{
	clear: left;
	margin: 0;
	padding: 0 20px;
	border: 0;
	text-align: left;
	border-top: 1px solid #f9f9f9;
	background-color: #fdfdfd;
	}

#footer p	{
	text-align: left;
	margin: 0;
	padding: 10px 0;
	font-size: x-small;
	background-color: transparent;
	color: #999;
	}


	/* Default links 	*/

a:link, a:visited {
	font-weight : bold;
	text-decoration : none;
	color: #692;
	background: transparent;
	}

a:hover {
	font-weight : bold;
	text-decoration : underline;
	color: #8b2;
	background: transparent;
	}

a:active {
	font-weight:bold;
	text-decoration:none;
	color:#7DD3A8;
	background:transparent;
	}


	/* Typography */

#main p, #sidebar p {
	line-height: 140%;
	margin-top: 5px;
	margin-bottom: 1em;
	}

.post-body {
  line-height: 140%;
  }

h1, h2, h3, h4, h5	{
	margin: 25px 0 0 0;
	padding: 0;
	}

h1.post-title {
	font-family:Gulim; font-size:13pt; font-weight:bold;
	margin-top:5px;
	}

h2.post-title {
	font-family:Gulim; font-size:12pt; font-weight:bold;
	margin-top:5px;
	}

ul.wasabi-ul {
	margin:0 0 25px 0;
	padding-left:30px;
	padding-top:3px;
	}

#recently li, #ArchiveList li {
	list-style: disc url(https://photos1.blogger.com/blogger/2921/1916/1600/diamond_blue.gif);
	vertical-align:bottom;
	line-height:160%;
	}

dl.profile-datablock	{
	margin: 3px 0 5px 0;
	}
dl.profile-datablock dd {
  line-height: 140%;
  }

.profile-img {display:inline;}

.profile-img img {
	float:left;
	margin:0 10px 5px 0;
	border:4px solid #8b2;
	}

#comments	{
	border: 0;
	border-top: 1px dashed #eed;
	margin: 10px 0 0 0;
	padding: 0;
	}

.comment-count	{
	font-family:'Tahoma'; font-size:14pt;
	margin-top:10px;
	margin-bottom:-10px;
	font-weight:normal;
	font-style:italic;
	text-transform:uppercase;
	letter-spacing:1px;
	}

#comments dl dt 	{
	font-weight: bold;
	font-style: italic;
	margin-top: 35px;
	padding: 1px 0 0 18px;
	background: transparent url('https://photos1.blogger.com/blogger/2921/1916/1600/commentbug.gif') top left no-repeat;
	color: #998;
	}

#comments dl dd	{
	padding: 0;
	margin: 0;
	}
.deleted-comment {
  font-style:italic;
  color:gray;
  }
.comment-link {
  margin-left:.6em;
  }


	/* Wasabi's */

#header_bottom_border { background:url('https://photos1.blogger.com/blogger/2921/1916/1600/headbotborder.gif') top left repeat-x; }

.date-header { font-family:'Tahoma'; font-size:13.5pt; font-weight:bold; margin-top:25px; margin-top:10px; }
.sidebar-title { font-family:'Tahoma'; font-size:13.5pt; font-weight:bold; margin-top:25px; }

hr { border-top:1px solid #9C9C9C; border-bottom:1px solid #F6F6F6; }
h3 { font-size:11pt; font-family:Dotum; font-weight:bold; }

.wasabi-fiction {
	font-family:Batang; text-align:justify; line-height:17pt; background-color:#FCFAF0;
	margin:0; padding:55px 50px 80px 50px; }

blockquote.wasabi-66 {
	background:url('https://photos1.blogger.com/blogger/2921/1916/1600/66.gif') no-repeat top left;
	padding-left:35px;
	margin:36px 30px 0px 10px; }

div.wasabi-p-decoration { background:url('https://photos1.blogger.com/blogger/2921/1916/1600/signature_gray.gif'); padding-top:20px; padding-bottom:100px; }
img.wasabi-p-decoration { float:left; margin:0px 10px 0px 10px; }

.wasabi-dropcap:first-letter {
	font-family:Batang, serif; font-size:48pt;
	line-height:1em;
	float:left; }

.wasabi-click-to-enlarge { font:9pt 'DotumChe'; color:#9C0CFC; letter-spacing:8pt }
.wasabi-cartoon { font-family:'MS Mincho'; font-size:12pt; line-height:1.2em }
.brokenLink { font:italic bold 9pt Arial; color:red }

.wasabi-h1 { font-size:24pt; line-height:1em }
.wasabi-h2 { font-size:18pt; line-height:1em }
.wasabi-h3 { font-size:11pt; font-family:Dotum; font-weight:bold; line-height:1em }
.wasabi-j-font { font-family:'MS Mincho', serif }
.wasabi-fc-gray-cool { color:#B4BFC4 }
.wasabi-fc-red { color:#FF0000 }
.wasabi-fc-blue { color:#0000FF }
.wasabi-fc-orange { color:#FFCC33 }
.wasabi-fc-orange-red { color:#FF9900 }
.wasabi-fc-red-cool { color:#F00077 }
.wasabi-fc-red { color:#FF0000 }

a.wsbNormal:link, a.wsbNormal:visited { font-weight:bold; text-decoration:none !important; color:#692; background:transparent !important; }
a.wsbNormal:hover { font-weight:bold; text-decoration:underline !important; color:#8b2 !important; background:transparent !important; }
a.wsbNormal:active { font-weight:bold; text-decoration:none !important; color:#7DD3A8 !important; background:transparent !important; }
#POST_AREA a:link, #POST_AREA a:visited { font-weight:bold; text-decoration:none; color:#78BC32; }
#POST_AREA a:hover, #POST_AREA a:active { font-weight:bold; text-decoration:none; color:#FFFFFF; background-color:#8AD839; }
a.wasabi-no-bg:hover, a.wasabi-no-bg:active { font-weight:bold; text-decoration:underline !important; color:#692 !important; background:transparent !important; }

a.wasabi-hover:hover { color:#FFFF8E; text-decoration:none }
a.wasabi-cool-hover:hover { text-decoration:none; border-bottom:1px dashed; color:#FE2790; }
a.wasabi-cool-hover:active { text-decoration:none; border-bottom:1px dashed; color:#FE2790; }
a.wasabi-no-uline:hover { text-decoration:none !important }
a.wasabi-push:hover { position:relative; top:1px; left:1px }
a.wasabi-ul-black:hover { text-decoration:underline; color:#000000; }
#ArchiveList a:hover,  #recently a:hover,  #AIListLinks a:hover  { text-decoration:none; border-bottom:1px dashed; color:#FE2790; }
#ArchiveList a:active, #recently a:active, #AIListLinks a:active { text-decoration:none; border-bottom:1px dashed; color:#FE2790; }
a.PTLink:link, a.PTLink:visited { color:black !important; background-color:white !important; }
a.PTLink:hover, a.PTLink:active { text-decoration:underline !important; color:black !important; background-color:white !important; }

#delicious-tags-mwultong a:link, #delicious-tags-mwultong a:visited, #delicious-tags-mwultong a:hover, #delicious-tags-mwultong a:active { font-weight:normal; }

.us-italic { font-family:'Georgia', serif; font-style:italic }
.us-bold { font-family:Arial, sans-serif; font-weight:bold }
.k-italic { font-style:italic; font-family:'Malgun Gothic'; }
.font-size10 { font-size:10pt }
.font-size12 { font-size:12pt }
.font-size24 { font-size:24pt }
.font-size72 { font-size:72pt }

em.wasabi-em { font-style:normal; border-bottom:1px dashed }
.wasabi-just { text-align:justify }
.wasabi-deleted { text-decoration:line-through; color:#C0C0C0 }
.wasabi-s-caps { font-variant:small-caps; }

.wasabi-img-border { border:2px solid blue }


.wasabi-tab { margin-left:3em; }
.wasabi-code { font-family:Fixedsys }
.wasabi-box { border:1px solid; padding:10px; }

.wasabi-code-scroll {
  font-family:Fixedsys, monospace;
  overflow:scroll; white-space:nowrap;
  width:103%; padding-bottom:10px;
  border-style:none;

  scrollbar-face-color:#FFFFFF;
  scrollbar-3dlight-color:#FFFFFF;
  scrollbar-highlight-color:#FFFFFF;
  scrollbar-shadow-color:#000000;
  scrollbar-darkshadow-color:#FFFFFF;
  scrollbar-arrow-color:#000000;
  scrollbar-track-color:#FFFFFF; }

.wasabi-code-box {
  font-family:DotumChe, monospace; font-size:10pt;
  background:#E2E2FF;
  overflow:scroll; white-space:nowrap;
  width:98%; padding:10px;

  scrollbar-face-color:#FFB9B9;
  scrollbar-3dlight-color:#FFB9B9;
  scrollbar-highlight-color:#FFFFFF;
  scrollbar-shadow-color:#FFFFFF;
  scrollbar-darkshadow-color:#FFB9B9;
  scrollbar-arrow-color:#FFFFFF;
  scrollbar-track-color:#FFEEEE; }

.wasabi-scroll-box {
  font-family:DotumChe, monospace; font-size:10pt;
  overflow:scroll; white-space:nowrap;
  width:98%; padding:10px;
  border:1px solid #C8C9FF; border-right-style:none; border-bottom-style:none;

  scrollbar-face-color:#C8C9FF;
  scrollbar-3dlight-color:#C8C9FF;
  scrollbar-highlight-color:#FFFFFF;
  scrollbar-shadow-color:#FFFFFF;
  scrollbar-darkshadow-color:#C8C9FF;
  scrollbar-arrow-color:#FFFFFF;
  scrollbar-track-color:#C8C9FF; }

.wasabi-console-box {
  font-family:DotumChe, monospace; font-size:10pt;
  background:#000000; color:#FFFFFF;
  overflow:scroll; white-space:nowrap;
  width:98%; padding:10px;
  border:1px solid #C5C5E6; border-right-style:none; border-bottom-style:none;

  scrollbar-face-color:#C5C5E6;
  scrollbar-3dlight-color:#C5C5E6;
  scrollbar-highlight-color:#FFFFFF;
  scrollbar-shadow-color:#FFFFFF;
  scrollbar-darkshadow-color:#C5C5E6;
  scrollbar-arrow-color:#FFFFFF;
  scrollbar-track-color:#C5C5E6; }

.wasabi-img-box {
  overflow:scroll;
  width:103%; padding-bottom:20px;
  border-style:none;

  scrollbar-face-color:#FFFFFF;
  scrollbar-3dlight-color:#FFFFFF;
  scrollbar-highlight-color:#FFFFFF;
  scrollbar-shadow-color:#000000;
  scrollbar-darkshadow-color:#FFFFFF;
  scrollbar-arrow-color:#000000;
  scrollbar-track-color:#FFFFFF; }

.wasabi-regex {
  font:24pt BatangChe;
  background-color:#FFDE66;
  padding:10pt; white-space:nowrap; width:97%; overflow:scroll; }

.wasabi-hscroll { height:auto; }

html {
  scrollbar-face-color:#66CDAA;
  scrollbar-3dlight-color:#66CDAA;
  scrollbar-highlight-color:#FFFFFF;
  scrollbar-shadow-color:#FFFFFF;
  scrollbar-darkshadow-color:#66CDAA;
  scrollbar-arrow-color:#FFFFFF;
  scrollbar-track-color:#E2F1EC; }


	/* Shortcuts */

.AIListDate {
	font:bold 10pt 'Arial';
	color:#FFBF00; }

.z-maBMK {
	font-size:8pt; font-weight:normal;
	color:#B6B6D5; }

.z-postedBy {
	font:italic bold 10pt 'Arial'; }

.z-pLink {
	font-family:Arial; font-style:normal;
	color:#99CC00; }

.z-LinkColorNormal { color:#669922; }




</style>


<script type="text/javascript">

// Disable country-specific URL
var blog = document.location.hostname;
var slug = document.location.pathname;
var ctld = blog.substr(blog.lastIndexOf("."));
if (ctld != ".com") {
    var ncr = "http://" + blog.substr(0, blog.indexOf("."));
    ncr += ".blogspot.com/ncr" + slug;
    window.location.replace(ncr);
}
// Disable country-specific URL


function maBMK(ItemPermalinkUrl, ItemTitle) {
  location.href='https://del.icio.us/post?v=4&amp;jump=no&amp;url='+encodeURIComponent(ItemPermalinkUrl)+'&amp;title='+encodeURIComponent(ItemTitle);
}



</script>



<!-- data-ad-client=ca-pub-7139050626890089 -->
<!-- --><style type="text/css">@import url(https://www.blogger.com/static/v1/v-css/navbar/3334278262-classic.css);
div.b-mobile {display:none;}
</style>

</head>
<body><script type="text/javascript">
    function setAttributeOnload(object, attribute, val) {
      if(window.addEventListener) {
        window.addEventListener('load',
          function(){ object[attribute] = val; }, false);
      } else {
        window.attachEvent('onload', function(){ object[attribute] = val; });
      }
    }
  </script>
<div id="navbar-iframe-container"></div>
<script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script>
<script type="text/javascript">
      gapi.load("gapi.iframes:gapi.iframes.style.bubble", function() {
        if (gapi.iframes && gapi.iframes.getContext) {
          gapi.iframes.getContext().openChild({
              url: 'https://www.blogger.com/navbar.g?targetBlogID\x3d19884063\x26blogName\x3dmwultong+Blog+...+%EB%94%94%EC%B9%B4+/+IT\x26publishMode\x3dPUBLISH_MODE_BLOGSPOT\x26navbarType\x3dTAN\x26layoutType\x3dCLASSIC\x26searchRoot\x3dhttps://mwultong.blogspot.com/search\x26blogLocale\x3den\x26v\x3d2\x26homepageUrl\x3dhttp://mwultong.blogspot.com/\x26vt\x3d-178875747451374039',
              where: document.getElementById("navbar-iframe-container"),
              id: "navbar-iframe"
          });
        }
      });
    </script>

<div></div> <!-- for IE7 -->

<!-- Begin wrapper -->
<div id="wrapper">

  <div id="blog-header"><span id="top"></span>
  <div class="myh1">

    

    

    
      <a href="http://mwultong.blogspot.com/" class="wasabi-hover wasabi-push">mwultong Blog ― 디카 / IT</a>
    

  </div> <!-- myh1 -->
  <p style="font:9pt Gulim; margin-top:6px;">컴퓨터 엑셀 워드 포토숍 구글어스 WINDOWS JAVASCRIPT JAVA C++</p>
  </div>
  <div id="header_bottom_border">&nbsp;</div>


<!-- Begin content -->
<div id="content">

  <!-- Begin main column -->
	<div id="main">




  <div style="text-align:right; margin-bottom:20px">
    <a href="#PP" class="wasabi-ul-black" title="직전 게시물"><span style="display:block; font:bold 10pt 'Tahoma'; color:black;"><span style="color:#FF8868;">P</span>revious <span style="color:#FFCC33">P</span>ost</span></a>
    <span><a href="http://mwultong.blogspot.com/2006/12/bashprofile-ubuntu-linux.html" class="wasabi-no-uline wasabi-push"><span style="font-weight:normal; color:#B3B8D2;">&#47532;&#45573;&#49828;] bash_profile &#54028;&#51068; &#49368;&#54540; &#50696;&#51228;: Ubuntu Linux</span></a></span><span style="display:none;"><a href="http://mwultong.blogspot.com/2006/12/c-print-string.html" class="wasabi-no-uline wasabi-push"><span style="font-weight:normal; color:#B3B8D2;">C&#50616;&#50612;] &#47928;&#51088;&#50676; &#52636;&#47141; &#54632;&#49688;; &#46020;&#49828; &#52285; &#54868;&#47732;&#50640; &#47928;&#51088;, &#49707;&#51088; &#52636;&#47141;; Print String</span></a></span><span style="display:none;"><a href="http://mwultong.blogspot.com/2006/12/c-float-to-int.html" class="wasabi-no-uline wasabi-push"><span style="font-weight:normal; color:#B3B8D2;">C&#50616;&#50612;] &#49548;&#49688;&#51216; &#51060;&#54616; &#48260;&#47532;&#44592;, &#49892;&#49688;&#47484; &#51221;&#49688;&#47196;; float to int</span></a></span><span style="display:none;"><a href="http://mwultong.blogspot.com/2006/12/javascript-float-to-int.html" class="wasabi-no-uline wasabi-push"><span style="font-weight:normal; color:#B3B8D2;">&#51088;&#48148;&#49828;&#53356;&#47549;&#53944;] &#49892;&#49688; &#49548;&#49688;&#51216; &#51060;&#54616; &#48260;&#47532;&#44592;, &#51221;&#49688;&#47196; &#47564;&#46300;&#45716; &#54632;&#49688;; JavaScript floa...</span></a></span><span style="display:none;"><a href="http://mwultong.blogspot.com/2006/12/perl-cwd-pwd-current-working-directory.html" class="wasabi-no-uline wasabi-push"><span style="font-weight:normal; color:#B3B8D2;">Perl/&#54148;] &#54788;&#51116; &#46356;&#47113;&#53664;&#47532; &#47749; &#44396;&#54616;&#44592;; &#46356;&#47113;&#53552;&#47532; &#50948;&#52824;; Cwd, pwd, Current ...</span></a></span><span style="display:none;"><a href="http://mwultong.blogspot.com/2006/12/perl-command-cmd-dos-shell.html" class="wasabi-no-uline wasabi-push"><span style="font-weight:normal; color:#B3B8D2;">Perl/&#54148;] COMMAND, CMD &#49892;&#54665;; &#46020;&#49828; &#49472;(DOS Shell) &#54840;&#52636; &#50696;&#51228;</span></a></span><span style="display:none;"><a href="http://mwultong.blogspot.com/2006/12/grep-back-slash.html" class="wasabi-no-uline wasabi-push"><span style="font-weight:normal; color:#B3B8D2;">grep ] &#48177; &#49836;&#47000;&#49772;(&#65340;) &#47928;&#51088;, Back Slash &#49438;&#51064; &#47928;&#51088;&#50676; &#52286;&#44592;; &#47532;&#45573;&#49828;/&#50976;&#45769;&#49828;</span></a></span><span style="display:none;"><a href="http://mwultong.blogspot.com/2006/12/tokyo-disneyland-google-earth.html" class="wasabi-no-uline wasabi-push"><span style="font-weight:normal; color:#B3B8D2;">&#46020;&#53188; &#46356;&#51592;&#45768;&#47004;&#46300;, &#50948;&#49457; &#49324;&#51652; &#44396;&#44544;&#50612;&#49828;; Tokyo Disneyland Google Earth</span></a></span><span style="display:none;"><a href="http://mwultong.blogspot.com/2006/12/google-earth-terrestrial-globe.html" class="wasabi-no-uline wasabi-push"><span style="font-weight:normal; color:#B3B8D2;">&#44396;&#44544; &#51648;&#44396;&#48376; &#54532;&#47196;&#44536;&#47016;, &#44396;&#44544; &#50948;&#49457;&#49324;&#51652; &#54868;&#47732;, &#45796;&#50868;&#47196;&#46300; &#51452;&#49548;; Google Earth Ter...</span></a></span><span style="display:none;"><a href="http://mwultong.blogspot.com/2006/12/html-css-tab-space-pre.html" class="wasabi-no-uline wasabi-push"><span style="font-weight:normal; color:#B3B8D2;">HTML-CSS] &#53485; &#47928;&#51088;(TAB) &#54364;&#54788;, &#44277;&#48177;(&#49828;&#54168;&#51060;&#49828;;Space) &#45347;&#44592;; PRE &#53468;&#44536;</span></a></span><span style="display:none;"></span>
  </div>










<!-- Begin .post -->
<div class="post"><a name="116503998969078521"></a>




<h1 class="post-title"><a href="http://mwultong.blogspot.com/2006/12/html-javascript-print-string.html" class="PTLink">자바스크립트] 문자열 출력 함수, 텍스트 쓰기; HTML-JavaScript Print String</a></h1>
<div class="date-header">Saturday, December 02, 2006</div>



스폰서 링크<br />
<div style="margin-top:10px;">
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- 자동_크기 -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-7139050626890089"
     data-ad-slot="7447856861"
     data-ad-format="auto"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>



<div id="POST_AREA">

<div class="post-body"><p><div style="clear:both;"></div>자바스크립트로 HTML에 문자열(글자)을 출력하려면<br /><strong>document.write();</strong><br />라는 메소드(함수)를 사용합니다.<br /><br />문자열이나 변수들을 서로 연결할 때에는 플러스(+) 기호나, 쉼표(,)로 이어 주면 됩니다.<br /><br />자바스크립트 안에서 따옴표를 사용할 때에는 작은따옴표(홑따옴표:')를 사용하는 것이 좋습니다. (<a href="http://mwultong.blogspot.com/2006/06/html-escape.html" title="mwultong Blog ― 소설 / IT">▶▶ [HTML] 자바스크립트 소스에서, 쌍따옴표 홑따옴표 (큰따옴표 작은따옴표) 표현 (이스케이프 Escape)</a> 참고)<br /><br />그리고<br />+ '&lt;br /&gt;'<br />이런 HTML 태그까지 출력해 주어야 다음 줄로 줄바꿈(행갈이)이 됩니다.<br /><br /><br /><h3>document.write: HTML 웹페이지에 글쓰기(문자열 출력) 예제</h3><br /><div class="wasabi-code-box">&lt;script type="text/javascript"&gt;<br /><br />document.writeln('글 쓰기 테스트입니다.');<br />document.write('글 쓰기 테스트입니다.' + '&lt;br /&gt;');<br />document.write('글 쓰기 테스트입니다.' + '&lt;br /&gt;');<br />document.write('글 쓰기 테스트입니다.' + '&lt;br /&gt;');<br /><br />// 빈 줄 3줄 넣기<br />document.write('&lt;br /&gt;&lt;br /&gt;&lt;br /&gt;');<br /><br /><br />var s = 'ABCD';<br />document.write('변수 내용 쓰기 테스트: ' + s + '&lt;br /&gt;');<br /><br /><br />var n = 123.001;<br />document.write('변수 내용 쓰기 테스트: ' + n + '&lt;br /&gt;');<br /><br /><br />// 또는 쉼표(콤마)로도, 문자열/변수를 서로 연결할 수 있음<br />document.write('변수 내용 쓰기 테스트: ', n, '&lt;br /&gt;');<br /><br />&lt;/script&gt;<br /></div><br /><br /><br />브라우저 화면 출력 결과:<br /><div class="wasabi-box">글 쓰기 테스트입니다. 글 쓰기 테스트입니다.<br />글 쓰기 테스트입니다.<br />글 쓰기 테스트입니다.<br /><br /><br /><br />변수 내용 쓰기 테스트: ABCD<br />변수 내용 쓰기 테스트: 123.001<br />변수 내용 쓰기 테스트: 123.001<br /></div><br /><br />document.writeln()<br />이라는 메서드는, 문자열을 출력한 후, 끝에 줄바꿈 문자를 추가하지만, HTML문법에서는 줄바꿈 문자가 무시되기에 실제로는 줄바꿈이 되지 않습니다.<br /><br /><br /><a href="http://del.icio.us/mwultong/html" rel="nofollow">☞ HTML/CSS/자바스크립트(JavaScript)</a><div style="clear:both; padding-bottom:0.25em"></div></p></div>

</div> <!-- POST_AREA -->

<p class="post-footer">
<span class="z-postedBy">
posted by mwultong <span style="color:#FF9900;">@</span> <a href="http://mwultong.blogspot.com/2006/12/html-javascript-print-string.html" class="wsbNormal" title="Permanent Link"><span class="z-LinkColorNormal">3:12 PM</span></a>
&nbsp;<a href="https://del.icio.us/post" onclick="location.href='https://del.icio.us/post?v=4&amp;jump=no&amp;url='+encodeURIComponent(location.href)+'&amp;title='+encodeURIComponent(&quot;자바스크립트] 문자열 출력 함수, 텍스트 쓰기; HTML-JavaScript Print String&quot;); return false;" class="wasabi-no-uline" title="온라인 즐겨찾기에 추가" rel="nofollow"><span style="color:#B6B6D5;">del.icio.us</span></a>
</span>




<span class="item-control blog-admin pid-331869048"><a style="border:none;" href="https://www.blogger.com/post-edit.g?blogID=19884063&postID=116503998969078521&from=pencil" title="Edit Post"><img class="icon-action" alt="" src="https://resources.blogblog.com/img/icon18_edit_allbkg.gif" height="18" width="18"></a></span>


<!-- Quick Search Start -->
<form id="google_search_quick" method="get" action="https://www.google.com/search">
  <input type="text" name="q" maxlength="255" value="" style="width:280px;" /> <input type="submit" name="btnG" value="Google 검색" style="width:110px;" />

  <input type="hidden" name="num" value="100" />
  <input type="hidden" name="domains" value="mwultong.blogspot.com" />
  <input type="hidden" name="sitesearch" value="mwultong.blogspot.com" />
</form>
<!-- Quick Search End -->


</p>


</div>
<!-- End .post -->



<!-- Begin #comments -->
 

  <div id="comments">

	<a name="comments"></a>

      <div class="comment-count">0 Comments:</div>

      <dl>
      
      </dl>

	<p>
    <span title="코멘트 쓰기"><a class="comment-link" href="https://www.blogger.com/comment.g?blogID=19884063&postID=116503998969078521">Post a Comment</a></span>
    </p>

  
    



	<p>
	<a href="http://mwultong.blogspot.com/" style="font-size:16pt;">&lt;&lt; Home</a>
	<a href="https://feeds.feedburner.com/mwultong" title="RSS 2.0 feed" rel="nofollow" target="_blank"><img src="https://photos1.blogger.com/blogger/2921/1916/1600/feed-icon16x16.png" style="margin-top:20px; margin-bottom:0px;" alt="RSS 2.0 feed" /></a>
    </p>
    </div>


<!-- End #comments -->
















<div style="margin-top:60px; padding:10px; font-size:9pt; border:1px dashed">구글 Google 에서 제공하는 무료 블로그 서비스인 블로거 Blogger 의 인터넷 주소는 <a href="https://www.blogger.com/" rel="nofollow" target="_blank">www.blogger.com</a> 입니다. Blogger 에 블로그를 만들면, <span style="font:bold 10pt 'Arial'">blogspot.com</span> 이라는 주소에 블로그가 생성됩니다.</div>

<div style="margin-top:10px; color:#A6B3DF; text-align:justify">블로그를 직접 방문하지 않고도 최신 게시물을 구독하려면 <a href="https://feeds.feedburner.com/mwultong" title="RSS 2.0 feed" rel="nofollow" target="_blank"><img src="https://photos1.blogger.com/blogger/2921/1916/1600/rss.gif" alt="RSS 2.0 feed" style="display:inline" /></a> 주소를 리더기에 등록하시면 됩니다.</div>

<div align="right" style="margin-right:152px; margin-top:60px;"><a href="#Category" class="wasabi-ul-black" title="게시물 분류"><span style="font:bold 10pt 'Tahoma'; color:black;"><span style="color:#6ACFAF">C</span>ategor<span style="color:#CACACA">ies</span></span></a></div>
<div align="right" style="margin-right:80px;"><a href="#PP" class="wasabi-ul-black" title="직전 게시물"><span style="font:bold 10pt 'Tahoma'; color:black;"><span style="color:#FF8868;">P</span>revious <span style="color:#FFCC33">P</span>osts</span></a></div>
<div align="right" style="margin-bottom:10px;"><a href="http://mwultong.blogspot.com/#MA" class="wasabi-ul-black" title="월별 게시물 목록" target="_blank"><span style="font-family:'Tahoma'; font-size:10pt; color:#000000;"><span style="color:#FF0000">M</span>onthly <span style="color:#00BFF3">A</span>rchives</span></a></div>




<div align="right" style="margin-bottom:10px;"><a href="#top" title="현재 페이지의 맨 위로">Top</a></div>


<!-- End main column -->
</div>




<div id="sidebar">

<!-- Begin #profile-container -->

<div id="profile-container">

<div class="sidebar-title"><span style="color:#FFC079">A</span>bout <span style="color:#C5C5E6">M</span>e</div>

<dl class="profile-datablock">
<dt class="profile-img"><a href="https://www.flickr.com/photos/mwultong/" rel="nofollow" target="_blank"><img src="//photos1.blogger.com/blogger/2921/1916/400/01051213.jpg" width="80" height="60"></a></dt>
<dd class="profile-data"><strong>Name:&nbsp;</strong> mwultong</dd>

<dd class="profile-data"><strong>Location:&nbsp;</strong> / 블로그 /</dd>
</dl>

<p class="profile-textblock">


구글 블로그 계정에서 운영되는 사이트입니다. 소프트웨어, 인터넷, 웹 디자인과 관련된 내용을 주로 다룹니다. 또한 일상적인 사진들을 고화질 이미지 파일로 업로드하고 있습니다. 디자인에 쓸 수 있는 색상표와, 각종 프로그램들의 사용법 설명과, 프로그래밍 언어들의 기초 강좌도 제공됩니다. 현재는, 브라우저에서 각종 단위를 환산할 수 있는 변환기 등, 학습이나 실생활과 직접 관련이 있는 내용을 포스팅하는 중입니다.
</p>

<img src="https://photos1.blogger.com/blogger/2921/1916/1600/signature.gif" style="margin-bottom:25px; margin-left:30px;" alt="Autograph" title="Autograph" />
<p class="profile-link"><a href="https://www.blogger.com/profile/11478802431579333732" rel="nofollow" target="_blank"><span class="wasabi-s-caps">View My Complete Profile</span></a></p>
</div>

    <!-- End #profile-container -->




<div id="Category" class="sidebar-title" title="게시물 분류"><span style="color:#6ACFAF;">C</span>ategor<span style="color:#CACACA;">ies</span></div>
<div style="margin-top:5px; margin-bottom:30px; margin-left:13px; line-height:1.7em;">

  <a href="https://del.icio.us/mwultong/perl" title="스크립트 언어: 펄" rel="nofollow" target="_blank">perl</a>
| <a href="https://del.icio.us/mwultong/blogger" title="blogger.com + blogspot.com 관련" rel="nofollow" target="_blank">blogger</a>
| <a href="https://del.icio.us/mwultong/books" title="독서" rel="nofollow" target="_blank">books</a>
| <a href="https://del.icio.us/mwultong/fiction" title="소설" rel="nofollow" target="_blank">소설</a>
| <a href="https://del.icio.us/mwultong/3dsmax" title="3ds Max &amp; 3D 그래픽" rel="nofollow" target="_blank">3dsmax</a>
| <a href="https://del.icio.us/mwultong/photoshop" title="Adobe Photoshop &amp; 2D Graphics" rel="nofollow" target="_blank">포토샵</a>
| <a href="https://del.icio.us/mwultong/chess" title="체스" rel="nofollow" target="_blank">chess</a>
| <a href="https://del.icio.us/mwultong/music" title="Music" rel="nofollow" target="_blank">음악</a>
| <a href="https://del.icio.us/mwultong/html" title="HTML/CSS/JavaScript" rel="nofollow" target="_blank">html / css</a>
| <a href="https://del.icio.us/mwultong/earth" title="Google Earth" rel="nofollow" target="_blank">구글어스</a>
| <a href="https://del.icio.us/mwultong/health" title="건강" rel="nofollow" target="_blank">health</a>
| <a href="https://del.icio.us/mwultong/living" title="생활 관련" rel="nofollow" target="_blank">living</a>
| <a href="https://del.icio.us/mwultong/windows" title="컴퓨터 OS 관련" rel="nofollow" target="_blank">윈도우</a>
| <a href="https://del.icio.us/mwultong/web" title="인터넷 서비스 관련" rel="nofollow" target="_blank">web</a>
| <a href="https://del.icio.us/mwultong/office" title="Excel Word Office" rel="nofollow" target="_blank">엑셀 워드</a>
| <a href="https://del.icio.us/mwultong/software" title="소프트웨어/유틸리티 사용법과 다운로드" rel="nofollow" target="_blank">software</a>
| <a href="https://del.icio.us/mwultong/security" title="보안" rel="nofollow" target="_blank">security</a>
| <a href="https://del.icio.us/mwultong/editor" title="텍스트 편집기" rel="nofollow" target="_blank">text editor</a>
| <a href="https://del.icio.us/mwultong/games" title="Game" rel="nofollow" target="_blank">게임</a>
| <a href="https://del.icio.us/mwultong/cpp" title="C/C++ 프로그래밍" rel="nofollow" target="_blank">c/c++</a>
| <a href="https://del.icio.us/mwultong/rss" title="RSS" rel="nofollow" target="_blank">rss</a>
| <a href="https://del.icio.us/mwultong/linux" title="리눅스/유닉스" rel="nofollow" target="_blank">linux / unix</a>
| <a href="https://del.icio.us/mwultong/mystery" title="UFO/예언 등" rel="nofollow" target="_blank">mystery</a>
| <a href="https://del.icio.us/mwultong/batch" title="배치 파일 / 각종 스크립트" rel="nofollow" target="_blank">batch</a>
| <a href="https://del.icio.us/mwultong/stamps" title="Postage Stamps / Philately" rel="nofollow" target="_blank">우표</a>
| <a href="https://del.icio.us/mwultong/study" title="일본어/영어/어학 관련" rel="nofollow" target="_blank">study</a>
| <a href="https://del.icio.us/mwultong/regex" title="정규식" rel="nofollow" target="_blank">regex</a>
| <a href="https://del.icio.us/mwultong/camera" title="사진/디카" rel="nofollow" target="_blank">카메라</a>
| <a href="https://del.icio.us/mwultong/python" title="파이썬" rel="nofollow" target="_blank">python</a>
| <a href="https://del.icio.us/mwultong/font" title="Fonts" rel="nofollow" target="_blank">폰트</a>
| <a href="https://del.icio.us/mwultong/java" title="자바" rel="nofollow" target="_blank">java</a>
| <a href="https://del.icio.us/mwultong/mathematica" title="매스매티카" rel="nofollow" target="_blank">mathematica</a>
| <a href="https://del.icio.us/mwultong/art" title="서양화" rel="nofollow" target="_blank">미술</a>
| <a href="https://del.icio.us/mwultong/php" title="PHP 프로그래밍" rel="nofollow" target="_blank">php</a>
| <a href="https://del.icio.us/mwultong/movie" title="비디오 클립" rel="nofollow" target="_blank">동영상</a>
| <a href="https://del.icio.us/mwultong/colors" title="색상표/배색표/디자인" rel="nofollow" target="_blank">colors</a>
| <a href="https://del.icio.us/mwultong/stock" title="Stock Market" rel="nofollow" target="_blank">주식투자</a>
| <a href="https://del.icio.us/mwultong/images" title="각종 이미지" rel="nofollow" target="_blank">사진</a>
| <a href="https://del.icio.us/mwultong/tools" title="온라인 단위 환산/변환기" rel="nofollow" target="_blank"><span style="color:#99CC00;">계산기</span></a>
| <a href="https://del.icio.us/mwultong/system:unfiled" title="미분류" rel="nofollow" target="_blank">...</a>

</div>

<div style="margin-bottom:30px;"><a href="https://del.icio.us/mwultong/z.cool" title="What's Cool" rel="nofollow" target="_blank"><span style="font:bold 10pt 'Tahoma'; color:black;"><span style="color:#B3B3FF">What</span>'s <span style="color:#FFB2B2">Cool</span></span> &nbsp; 인기/추천 게시물</a></div>









  <div id="PP" class="sidebar-title" title="직전 게시물"><span style="color:#FF8868">P</span>revious <span style="color:#FFCC33">P</span>osts</div>



  <ul id="recently" class="wasabi-ul">
    
        <li><a href="http://mwultong.blogspot.com/2006/12/bashprofile-ubuntu-linux.html">&#47532;&#45573;&#49828;] bash_profile &#54028;&#51068; &#49368;&#54540; &#50696;&#51228;: Ubuntu Linux</a></li>
     
        <li><a href="http://mwultong.blogspot.com/2006/12/c-print-string.html">C&#50616;&#50612;] &#47928;&#51088;&#50676; &#52636;&#47141; &#54632;&#49688;; &#46020;&#49828; &#52285; &#54868;&#47732;&#50640; &#47928;&#51088;, &#49707;&#51088; &#52636;&#47141;; Print String</a></li>
     
        <li><a href="http://mwultong.blogspot.com/2006/12/c-float-to-int.html">C&#50616;&#50612;] &#49548;&#49688;&#51216; &#51060;&#54616; &#48260;&#47532;&#44592;, &#49892;&#49688;&#47484; &#51221;&#49688;&#47196;; float to int</a></li>
     
        <li><a href="http://mwultong.blogspot.com/2006/12/javascript-float-to-int.html">&#51088;&#48148;&#49828;&#53356;&#47549;&#53944;] &#49892;&#49688; &#49548;&#49688;&#51216; &#51060;&#54616; &#48260;&#47532;&#44592;, &#51221;&#49688;&#47196; &#47564;&#46300;&#45716; &#54632;&#49688;; JavaScript floa...</a></li>
     
        <li><a href="http://mwultong.blogspot.com/2006/12/perl-cwd-pwd-current-working-directory.html">Perl/&#54148;] &#54788;&#51116; &#46356;&#47113;&#53664;&#47532; &#47749; &#44396;&#54616;&#44592;; &#46356;&#47113;&#53552;&#47532; &#50948;&#52824;; Cwd, pwd, Current ...</a></li>
     
        <li><a href="http://mwultong.blogspot.com/2006/12/perl-command-cmd-dos-shell.html">Perl/&#54148;] COMMAND, CMD &#49892;&#54665;; &#46020;&#49828; &#49472;(DOS Shell) &#54840;&#52636; &#50696;&#51228;</a></li>
     
        <li><a href="http://mwultong.blogspot.com/2006/12/grep-back-slash.html">grep ] &#48177; &#49836;&#47000;&#49772;(&#65340;) &#47928;&#51088;, Back Slash &#49438;&#51064; &#47928;&#51088;&#50676; &#52286;&#44592;; &#47532;&#45573;&#49828;/&#50976;&#45769;&#49828;</a></li>
     
        <li><a href="http://mwultong.blogspot.com/2006/12/tokyo-disneyland-google-earth.html">&#46020;&#53188; &#46356;&#51592;&#45768;&#47004;&#46300;, &#50948;&#49457; &#49324;&#51652; &#44396;&#44544;&#50612;&#49828;; Tokyo Disneyland Google Earth</a></li>
     
        <li><a href="http://mwultong.blogspot.com/2006/12/google-earth-terrestrial-globe.html">&#44396;&#44544; &#51648;&#44396;&#48376; &#54532;&#47196;&#44536;&#47016;, &#44396;&#44544; &#50948;&#49457;&#49324;&#51652; &#54868;&#47732;, &#45796;&#50868;&#47196;&#46300; &#51452;&#49548;; Google Earth Ter...</a></li>
     
        <li><a href="http://mwultong.blogspot.com/2006/12/html-css-tab-space-pre.html">HTML-CSS] &#53485; &#47928;&#51088;(TAB) &#54364;&#54788;, &#44277;&#48177;(&#49828;&#54168;&#51060;&#49828;;Space) &#45347;&#44592;; PRE &#53468;&#44536;</a></li>
     
  </ul>








<!-- SiteSearch Google Start -->
<form id="google_search" method="get" action="https://www.google.com/search" target="_blank">
<table>
  <tr><td align="center"><img src="https://www.google.com/logos/Logo_40wht.gif" alt="Google" /></td></tr>
  <tr><td align="center">
          <input type="hidden" name="num" value="100" />
          <input type="text" name="q" size="31" maxlength="255" value="" style="color:#000000; background-color:#FFFFFF;" />
      </td>
  </tr>
  <tr><td align="center">
          <input type="hidden" name="domains" value="mwultong.blogspot.com" />
          <input type="radio" name="sitesearch" value="" /> <span style="font:10pt 'Tahoma';">WWW</span>
          <input type="radio" name="sitesearch" value="mwultong.blogspot.com" checked="checked" /> <span style="font:10pt 'Tahoma';">mwultong Blog</span>
      </td>
  </tr>
  <tr><td align="center"><input type="submit" name="btnG" value="Google 검색" style="margin-top:7px;" /></td>
  </tr>
</table>
</form>
<!-- SiteSearch Google End -->




<p id="powered-by" style="margin-bottom:30px;"><a href="https://www.blogger.com/" rel="nofollow" target="_blank"><img src="https://lh3.google.com/image/mwultong/RkPaFP5HqvI/AAAAAAAAAGs/gx9HIILnSUg/s144/bloggerbutton1.gif" alt="Powered by Blogger" /></a></p>











    <!--
    <p>This is a paragraph of text that could go in the sidebar.</p>
    -->

  <!-- End sidebar -->
  </div>

<!-- End content -->
</div>


<div id="footer">

</div>


<!-- End wrapper -->
</div>




</body>
</html>
"""}
    return render(request, "page/show_html.html", context)