package com.dpmo.test;
import org.springframework.beans.factory.annotation.Autowired;
import java.util.List;
import org.springframework.stereotype.Service;

@Service
public class TenderToHandoverService {

	@Autowired
	private TenderToHandoverRepository tendertohandoverRepository;

	public List<TenderToHandoverEntity> getAll() {
		return tendertohandoverRepository.findAll();	}

	public TenderToHandoverEntity getTenderToHandoverById(int id) {
		return tendertohandoverRepository.findById(id);
	}

	public void addTenderToHandover(TenderToHandoverEntity tendertohandover) {
		tendertohandoverRepository.save(tendertohandover);
	}

	public void updateTenderToHandover(TenderToHandoverEntity tendertohandover) {
		tendertohandoverRepository.save(tendertohandover);
	}

	public void deleteTenderToHandover(int id) {
		tendertohandoverRepository.delete(tendertohandoverRepository.findById(id));
	}

	public TenderToHandoverEntity getTenderToHandoverByCamelCase(String camelCase) {
		return tendertohandoverRepository.findOneByCamelCase(camelCase);
	}

	public TenderToHandoverEntity getTenderToHandoverByTestEncore(String testEncore) {
		return tendertohandoverRepository.findOneByTestEncore(testEncore);
	}

}