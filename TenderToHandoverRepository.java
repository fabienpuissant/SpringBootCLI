package com.dpmo.test;
import org.springframework.data.repository.CrudRepository;
import java.util.List;
import org.springframework.stereotype.Repository;
import com.dpmo.test.TenderToHandoverEntity;

@Repository 
public interface TenderToHandoverRepository extends CrudRepository<TenderToHandoverEntity, Integer> {

	 public List<TenderToHandoverEntity> findAll();

	 public TenderToHandoverEntity findById(int id);

	public TenderToHandoverEntity findOneByCamelCase(String camelCase);

	public TenderToHandoverEntity findOneByTestEncore(String testEncore);

}