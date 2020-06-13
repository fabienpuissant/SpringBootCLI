package user;
import org.springframework.beans.factory.annotation.Autowired;
import java.util.List;
import org.springframework.stereotype.Service;

@Service
public class UserService {

	@Autowired
	private UserRepository userRepository;

	public List<UserEntity> getAll() {
		return userRepository.findAll();	}

	public UserEntity getUserById(int id) {
		return userRepository.findById(id);
	}

	public void addUser(UserEntity user) {
		userRepository.save(user);
	}

	public void updateUser(UserEntity user) {
		userRepository.save(user);
	}

	public void deleteUser(int id) {
		userRepository.delete(userRepository.findById(id));
	}

	public UserEntity getUserByPrenom(String prenom) {
		return userRepository.findOneByPrenom(prenom);
	}

	public UserEntity getUserByNom(String nom) {
		return userRepository.findOneByNom(nom);
	}

}