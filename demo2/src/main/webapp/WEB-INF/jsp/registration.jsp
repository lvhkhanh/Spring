<!DOCTYPE html>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<%@ taglib prefix="spring" uri="http://www.springframework.org/tags" %>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Registration from jsp</title>
</head>
<body>
    <h1>${message}</h1>
    <form:form  modelAttribute="registration">
    <spring:message code="name" />
    <form:input path="name">
    <input type="submit" value="Add">
    </form:form>
</body>
</html>