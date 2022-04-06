package com.codingdojo.bookclub.repositories;

import java.util.List;
import java.util.Optional;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.codingdojo.bookclub.models.Book;

@Repository
public interface BookRepository extends CrudRepository<Book, Long> {
	
	
	Optional<Book> findById(Long id);
	
	List<Book> findAll();
	
	void deleteById(Long id);

	// Book save(Book b)
	
}
