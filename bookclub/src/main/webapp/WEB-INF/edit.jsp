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
<title>Title Here</title>
  <!-- Bootstrap -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" 
      rel="stylesheet" 
      integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" 
      crossorigin="anonymous">

</head>
<body>
    <div class="container"> <!-- Beginning of Container -->
    	
    	<a href="logout" class="btn btn-danger mt-2 float-end">Logout</a>
    	<a href="/home" class="btn btn-success mt-2 mr-2 float-end">Home</a>
        <br><br><br>
	<h1>Editing <c:out value="${book.title}"></c:out></h1><br><br>
	<form:form action="/update/${book.id}" method="post" modelAttribute="book">
	<input type="hidden" name="_method" value="put" />
		<form:hidden path="reader"/>
	    <p>
	        <form:label path="title">Title</form:label>
	        <p class="text-danger"><form:errors path="title"/></p>
	        <form:input path="title"/>
	    </p>
	    
	    <p>
	        <form:label path="authorName">Author</form:label>
	        <p class="text-danger"><form:errors path="authorName"/></p>
	        <form:input path="authorName"/>
	    </p>
	    <p>
	        <form:label path="amount">Amount</form:label>
	        <p class="text-danger"><form:errors path="amount"/></p>     
	        <form:input type="number" path="amount"/>
	    </p>    
	    <p>
	        <form:label path="thought">My Thoughts</form:label>
	        <p class="text-danger"><form:errors path="thought"/></p>
	        <form:textarea path="thought"/>
	    </p>
	    <input class="btn btn-info mt-2" type="submit" value="Update Book"/>
	</form:form>
	<br><br>
		<form action="/delete/${book.id}" method="post">
    		<input type="hidden" name="_method" value="delete">
    		<input class="btn btn-danger" type="submit" value="Delete">
		</form>
    </div> <!-- End of Container -->
</body>
</html>