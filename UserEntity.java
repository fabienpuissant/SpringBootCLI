package user;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "user_entity")

public class UserEntity {

	@Id
	@GeneratedValue(strategy=GenerationType.AUTO)
	private Integer id;

	@Column
	private String prenom;

	@Column
	private String nom;

	public UserEntity () { 

    	}

	public String getPrenom() {
		return prenom;
	}

	public void setPrenom(String prenom) {
		this.prenom = prenom;
	} 

	public String getNom() {
		return nom;
	}

	public void setNom(String nom) {
		this.nom = nom;
	} 

}