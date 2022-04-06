package com.codingdojo.bookclub.controllers;

import java.util.List;

import javax.servlet.http.HttpSession;
import javax.validation.Valid;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import com.codingdojo.bookclub.models.Book;
import com.codingdojo.bookclub.models.LoginUser;
import com.codingdojo.bookclub.models.User;
import com.codingdojo.bookclub.services.BookService;
import com.codingdojo.bookclub.services.UserService;

@Controller
public class MainController {
	
	 
	    private UserService userServ;
	    private final BookService bookServ;
	    public MainController(UserService userServ, BookService bookServ) {
	    	this.userServ = userServ;
	    	this.bookServ = bookServ;
	    }
	    
	    @GetMapping("/")
	    public String index(Model model) {
	        model.addAttribute("newUser", new User());
	        model.addAttribute("newLogin", new LoginUser());
	        return "index.jsp";
	    }
	    
	    @PostMapping("/register")
	    public String register(@Valid @ModelAttribute("newUser") User newUser, BindingResult result, 
	    		Model model, HttpSession session) {
	        userServ.register(newUser, result);
	        if(result.hasErrors()) {
	            model.addAttribute("newLogin", new LoginUser());
	            return "index.jsp";
	        }
	        session.setAttribute("user_id", newUser.getId());
	        return "redirect:/home";
	    }
	    
	    @PostMapping("/login")
	    public String login(@Valid @ModelAttribute("newLogin") LoginUser newLogin, BindingResult result, 
	    		Model model, HttpSession session) {
	        User user = userServ.login(newLogin, result);
	        if(result.hasErrors()) {
	            model.addAttribute("newUser", new User());
	            return "index.jsp";
	        }
	        session.setAttribute("user_id", user.getId());
	        return "redirect:/home";
	    }
	    
	    
	    @GetMapping("/logout")
	    public String logout(HttpSession session) {
	    	session.invalidate();
	    	return "redirect:/";
	    }
	    
	    @GetMapping("/home")
	    public String dashborad(HttpSession session, Model model, RedirectAttributes flash) {
	    	Long userId = (Long) session.getAttribute("user_id");
	    	if(userId == null) {
	    		flash.addFlashAttribute("login", "Please Login!");
	    		return "redirect:/";}
	    	
	    	User user = userServ.getUserInfo(userId);
	    	model.addAttribute("loggedUser", user);
	    	
	    	List<Book> books = bookServ.getAllBooks();
	    	model.addAttribute("books", books);
	    	
	    	return "dashboard.jsp";
	    }
	    
	    
	    @GetMapping("/new")
	    public String newBook(HttpSession session, Model model, RedirectAttributes flash) {
	    	Long userId = (Long) session.getAttribute("user_id");
	    	if(userId == null) {
	    		flash.addFlashAttribute("login", "Please Login!");
	    		return "redirect:/";
	    		}
	    	
	    	model.addAttribute("userId", userId);
	    	model.addAttribute("book", new Book());
	    	return "new.jsp";
	    }
	    
	    
	    @PostMapping("/create")
	    public String createBook(@Valid @ModelAttribute("book") Book book, BindingResult result, HttpSession session, Model model){
	    	if(result.hasErrors()) {
	    		Long userId = (Long) session.getAttribute("user_id");
	    		model.addAttribute("userId", userId);
	    		return "new.jsp";
	    	}else {
	    		bookServ.saveBook(book);
	    		return "redirect:/home";
	    	}
	    	
	    }
	    
	    
	    
	    @GetMapping("/show/{id}")
	    public String showBook(@PathVariable("id") Long bookId, HttpSession session, Model model, RedirectAttributes flash) {
	    	Long userId = (Long) session.getAttribute("user_id");
	    	if(userId == null) {
	    		flash.addFlashAttribute("login", "Please Login!");
	    		return "redirect:/";}
	    	
	    	Book book = bookServ.findOneBook(bookId);
	    	model.addAttribute("book", book);
	    	
	    	
	    	return "show.jsp";
	    }
	    
	    
	    
	    @GetMapping("/edit/{id}")
	    public String editBook(@PathVariable("id") Long bookId, HttpSession session, Model model, RedirectAttributes flash) {
	    	Long userId = (Long) session.getAttribute("user_id");
	    	if(userId == null) {
	    		flash.addFlashAttribute("login", "Please Login!");
	    		return "redirect:/";}
	    	
	    	Book book = bookServ.findOneBook(bookId);
	    	if(book.getReader().getId().equals(userId) ) {
	    		model.addAttribute("book", book);
		    	return "edit.jsp";
	    	}
	    	flash.addFlashAttribute("reader", "You must be the reader to edit book");
	    	return "redirect:/home";
	    }
	    
	    
	    @PutMapping("/update/{id}")
	    public String updateBook(@Valid @ModelAttribute("book") Book book, BindingResult result, HttpSession session, Model model){
	    	if(result.hasErrors()) {
	    		return "edit.jsp";
	    	}else {
	    		bookServ.saveBook(book);
	    		return "redirect:/home";
	    	}
	    	
	    }
	    
	    
	    @DeleteMapping("/delete/{id}")
	    public String deleteBook(@PathVariable("id") Long bookId, HttpSession session, Model model, RedirectAttributes flash) {
	    	Long userId = (Long) session.getAttribute("user_id");
	    	if(userId == null) {
	    		flash.addFlashAttribute("login", "Please Login!");
	    		return "redirect:/";}
	    	
	    	Book book = bookServ.findOneBook(bookId);
	    	if(book.getReader().getId().equals(userId) ) {
	    		bookServ.deleteBook(bookId);
		    	return "redirect:/home";
	    	}
	    	flash.addFlashAttribute("reader", "You must be the reader to delete book");
	    	return "redirect:/home";
	    }
	    
	   
	    
}

