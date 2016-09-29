package BackendBob;

import java.util.LinkedList;
import java.util.List;

public class Buyer  implements  Runnable  {
	String name;
	List<Integer> prices = new LinkedList<>();
	Auction auction;
	

	public Buyer(String name,List<Integer> prices, Auction auction){
		this.name = name;
		this.prices = prices;
		this.auction = auction;
	}


	@Override
	public void run() {
		for(Integer price: prices){
			Bid bid = new Bid(name, price);
			auction.addBid(bid);
			try {
				Thread.sleep(10);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}

		}
		
	}

}
