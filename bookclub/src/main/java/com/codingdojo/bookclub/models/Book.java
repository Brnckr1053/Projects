package com.codingdojo.bookclub.models;

import java.util.Date;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.PrePersist;
import javax.persistence.PreUpdate;
import javax.persistence.Table;
import javax.validation.constraints.Min;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;

import org.springframework.format.annotation.DateTimeFormat;

@Entity
@Table(name="books")
public class Book {

	@Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
	
	@NotNull
	@Size(min=3, max=30, message="Book title must be between 3 and 30 characters")
	private String title;
	
	@NotNull
	@Size(min=2, max=30, message="Author Name must be between 2 and 30 characters")
	private String authorName;
	
	@NotNull
    @Min(value=10, message="Amount must be more than 10 dolars.")
    private Integer amount;
	
    @NotNull
    @Size(min = 5, max = 200, message="Your thoughts must be at least 5 characters.")
    private String thought;
	
	@Column(updatable=false)
	@DateTimeFormat(pattern="yyyy-MM-dd")
	private Date createdAt;
    @DateTimeFormat(pattern="yyyy-MM-dd")
    private Date updatetedAt;
    
    @PrePersist
    protected void onCreate() {
    	this.createdAt = new Date();
    }
    @PreUpdate
    protected void onUpdate() {
    	this.updatetedAt = new Date();
    }
	
	
    
    @ManyToOne(fetch=FetchType.LAZY)
    @JoinColumn(name="reader_id")
    private User reader;
    
    
    public Book() {}
	public Long getId() {
		return id;
	}
	
	
	
	
	public Book(Long id,
			@NotNull @Size(min = 3, max = 30, message = "Book title must be between 3 and 30 characters") String title,
			@NotNull @Size(min = 2, max = 30, message = "Author Name must be between 2 and 30 characters") String authorName,
			@NotNull @Min(value = 10, message = "Amount must be more than 10 dolars.") Integer amount,
			@NotNull @Size(min = 5, max = 200, message = "Your thoughts must be at least 5 characters.") String thought,
			User reader) {
		this.id = id;
		this.title = title;
		this.authorName = authorName;
		this.amount = amount;
		this.thought = thought;
		this.reader = reader;
	}
	
	
	public void setId(Long id) {
		this.id = id;
	}
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public String getAuthorName() {
		return authorName;
	}
	public void setAuthorName(String authorName) {
		this.authorName = authorName;
	}
	public Integer getAmount() {
		return amount;
	}
	public void setAmount(Integer amount) {
		this.amount = amount;
	}
	public String getThought() {
		return thought;
	}
	public void setThought(String thought) {
		this.thought = thought;
	}
	public User getReader() {
		return reader;
	}
	public void setReader(User reader) {
		this.reader = reader;
	}
    
    
	
}
