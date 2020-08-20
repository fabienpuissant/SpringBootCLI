package com.dpmo.test;
import org.springframework.http.MediaType;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TenderToHandoverRestController {

	@Autowired
	private TenderToHandoverService tendertohandoverService;

	@GetMapping("TenderToHandoverService/{id}")
	public TenderToHandoverEntity getUserById(@PathVariable int id) { 
		 return tendertohandoverService.getTenderToHandoverById(id);	}

	@PostMapping(value="TenderToHandoverService/addTenderToHandover", consumes=MediaType.APPLICATION_JSON_VALUE)
	public void addTenderToHandover(@RequestBody TenderToHandoverEntity tendertohandover) { 
		tendertohandoverService.addTenderToHandover(tendertohandover);
	}

	@DeleteMapping("TenderToHandoverService/delete/{id}")
	public void deleteByIdTenderToHandover(@PathVariable int id) { 
		tendertohandoverService.deleteTenderToHandover(id);
	}

}