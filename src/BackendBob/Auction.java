package BackendBob;

import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.concurrent.ConcurrentLinkedQueue;

public class Auction {

	ObjectToSell object;
	Queue<Bid> globalBids = new ConcurrentLinkedQueue<>();
	Bid winner = null;
	Boolean auctionRunning = false;

	public Auction(ObjectToSell object){
			this.object = object;
	}

	public void addBid(Bid bid){
		if(bid.price >= object.reservedPrice){
			globalBids.add(bid);
		}
	}
	
	public synchronized void launchAuction(List<Buyer> buyers) throws InterruptedException{
		if(!auctionRunning){
			auctionRunning = true;
			List<Thread> runningBuyers = new ArrayList<>();
			for(Buyer buyer: buyers){
				Thread thread = new Thread(buyer);
				runningBuyers.add(thread);
				thread.start(); 
			}
			while(stillBidding(runningBuyers)){
				Thread.sleep(10);
			}
			// When auction is over
			selectAuctionWinner();
			auctionRunning = false;
		}
		else{
			System.out.println("Auction already running");
		}
	}
	
	boolean stillBidding(List<Thread> runningBuyers ){
		for(Thread runningBuyer: runningBuyers ){
			if(runningBuyer.isAlive()){
				return true;
			}
		}
		return false;
	}
	
	//THE algorithm
	public void selectAuctionWinner(){		
		int sellingPrice = object.reservedPrice;
		int winnerPrice = object.reservedPrice; 
		
		while(!globalBids.isEmpty()){
			Bid bid = globalBids.remove();
			if(bid.price > winnerPrice){
				winnerPrice = bid.price;
				winner = bid;
			}else{
				if(bid.price > sellingPrice){
					sellingPrice = bid.price;
				}
			}
		}
		if(winner != null){
			winner.price = sellingPrice;
		}
	}
}
