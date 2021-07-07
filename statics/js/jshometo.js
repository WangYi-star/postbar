// JavaScript Document
// function black(){
// 	// window.open ("commit.html", "newwindow", "height=100, width=400, toolbar=no, menubar=no, scrollbars=no, resizable=no, location=no, status=no");
// 	window.open ("../templates/commit.html", "newwindow", "height=100, width=400, toolbar=no, menubar=no, scrollbars=no, resizable=no, location=no, status=no");
// }

function black(postid) {
	window.open ("/hometo/commit?postid="+postid.value,"newwindow","height=330, width=500, top=100,left=500, toolbar=no, menubar=no, scrollbars=no, resizable=no, location=no, status=no");
}
function blackbug(postid) {
	window.open ("/hometo/commit_bug?postid="+postid.value,"newwindow","height=330, width=500, top=100,left=500, toolbar=no, menubar=no, scrollbars=no, resizable=no, location=no, status=no");
}