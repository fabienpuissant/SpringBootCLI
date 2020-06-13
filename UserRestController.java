package user;
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
public class UserRestController {

	@Autowired
	private UserService userService;

	@GetMapping("UserService/{id}")
	public UserEntity getUserById(@PathVariable int id) { 
		 return userService.getUserById(id);	}

	@PostMapping(value="UserService/addUser", consumes=MediaType.APPLICATION_JSON_VALUE)
	public void addUser(@RequestBody UserEntity user) { 
		userService.addUser(user);
	}

	@DeleteMapping("UserService/delete/{id}")
	public void deleteByIdUser(@PathVariable int id) { 
		userService.deleteUser(id);
	}

}