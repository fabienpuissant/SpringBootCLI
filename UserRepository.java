package user;
import org.springframework.data.repository.CrudRepository;
import java.util.List;
import user.UserEntity;

public interface UserRepository extends CrudRepository<UserEntity, Integer> {

	 public List<UserEntity> findAll();

	 public UserEntity findById(int id);

	public UserEntity findOneByPrenom(String Prenom);

	public UserEntity findOneByNom(String Nom);

}