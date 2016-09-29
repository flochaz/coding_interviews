package BackendBob;

public class Bid {
	public String buyerName;
	public int price;
	
	public Bid(String buyerName, int price){
		this.buyerName = buyerName;
		this.price = price;
	}

	public String toString(){
		return "Bid by " + buyerName + " at price => " + price;
	}
}
