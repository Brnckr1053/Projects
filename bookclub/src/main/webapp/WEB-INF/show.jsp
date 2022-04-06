<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    
   <!-- c:out ; c:forEach ; c:if -->
 <%@taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%> 
   <!-- Formatting (like dates) -->
 <%@taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt"%>
   <!-- form:form -->
 <%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>  
   <!-- for rendering errors on PUT routes -->
 <%@ page isErrorPage="true" %>   
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Book</title>
  <!-- Bootstrap -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" 
      rel="stylesheet" 
      integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" 
      crossorigin="anonymous">

</head>
<body>
    <div class="container"> <br><br><!-- Beginning of Container -->
        <h1><c:out value="${book.title}"></c:out></h1><br>
        
        <a href="logout" class="btn btn-danger mt-2 mr-2 float-end">Logout</a>
        <a href="/home" class="btn btn-success mt-2 mr-2 float-end">Home</a>
        
        
        
        	<h2><c:out value="${book.reader.firstName}"></c:out> read <c:out value="${book.title}"></c:out> by <c:out value="${book.authorName}"></c:out>.</h2>
        	<p>Here are <c:out value="${book.reader.firstName}"></c:out>'s thoughts : </p>
        	
        	<p><c:out value="${book.thought}"></c:out></p>
        	<p>Amount : $<c:out value="${book.amount}"></c:out></p>
        	<br><br>
        	<a href="/edit/${book.id}" class="btn btn-primary"> Edit </a>

		       	<form action="/delete/${book.id}" method="post">
    				<input type="hidden" name="_method" value="delete">
    				<input class="btn btn-danger" type="submit" value="Delete">
				</form>
        	
        	
        	
        
        
    </div> <!-- End of Container -->
</body>
</html>