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
        <h1>Hello, <span class="text-info"><c:out value="${loggedUser.firstName}"></c:out></span></h1>
        <a href="/new" class="btn btn-warning mt-2">+Add to my shelf!!</a><br><br>
        <p class="text-danger"><c:out value="${reader}"></c:out></p>
        
        <table class="table table-hover">
		  <thead>
		    <tr>
		      <th scope="col">#</th>
		      <th scope="col">Title</th>
		      <th scope="col">Author Name</th>
		      <th scope="col">Posted By</th>
		      <th scope="col">Actions</th>
		    </tr>
		  </thead>
		  <tbody>
		  <c:forEach var="book" items="${books}">
		    <tr>
		      <th scope="row"><c:out value="${book.id}"></c:out></th>
		      <td><a href="/show/${book.id}"><c:out value="${book.title}"></c:out></a></td>
		      <td><c:out value="${book.authorName}"></c:out></td>
		      <td><c:out value="${book.reader.firstName}"></c:out></td>
		      <td>
			    <a href="/edit/${book.id}" class="btn btn-primary"> Edit </a>
		      	|
		       	<form action="/delete/${book.id}" method="post">
    				<input type="hidden" name="_method" value="delete">
    				<input class="btn btn-danger" type="submit" value="Delete">
				</form>
		       </td>
		    </tr>
		  </c:forEach>
		  </tbody>
		</table>
        
    </div> <!-- End of Container -->
</body>
</html>