package com.dpmo.test;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "aa")

public class TenderToHandoverEntity {

	@Id
	@GeneratedValue(strategy=GenerationType.AUTO)
	private Integer id;

	@Column
	private String camelCase;

	@Column
	private String testEncore;

	public TenderToHandoverEntity () { 

    	}

	public String getCamelCase() {
		return camelCase;
	}

	public void setCamelCase(String camelCase) {
		this.camelCase = camelCase;
	} 

	public String getTestEncore() {
		return testEncore;
	}

	public void setTestEncore(String testEncore) {
		this.testEncore = testEncore;
	} 

}