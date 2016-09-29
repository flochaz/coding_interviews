package BackendBob;

import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

import org.junit.Before;
import org.junit.Test;

public class AuctionTest {

	int reservedPrice = 100;
	@Before
	public void SetUp(){
		
	}
	
	@Test
	public void zeroBidTest() throws InterruptedException{
		ObjectToSell object = new ObjectToSell(reservedPrice);
		Auction objectAuction = new Auction(object);

		List<Buyer> buyers = new ArrayList<>();
		List<Integer> emptyList = new LinkedList<>();
		Buyer a = new Buyer("A", emptyList, objectAuction);

		buyers.add(a);
	
		objectAuction.launchAuction(buyers);
		
		assertNull(objectAuction.winner);	}
	
	@Test
	public void noBidOverReservedPriceTest() throws InterruptedException{
		ObjectToSell object = new ObjectToSell(reservedPrice);
		Auction objectAuction = new Auction(object);
		List<Buyer> buyers = new ArrayList<>();
		List<Integer> lowBids = new LinkedList<>();
		
		lowBids.add(90);
		// following requirement, ABOVE "The buyer winning the auction is the one with the highest bid above the reserve price."
		lowBids.add(reservedPrice);
		Buyer a = new Buyer("A", lowBids, objectAuction);
		buyers.add(a);
		objectAuction.launchAuction(buyers);
		
		assertNull(objectAuction.winner);
	}
	
	@Test
	public void BidAtReservedPriceTest() throws InterruptedException{
		ObjectToSell object = new ObjectToSell(reservedPrice);
		Auction objectAuction = new Auction(object);

		List<Buyer> buyers = new ArrayList<>();
		List<Integer> lowBids = new LinkedList<>();
		lowBids.add(reservedPrice + 1);
		Buyer a = new Buyer("A", lowBids, objectAuction);
		buyers.add(a);
		
		objectAuction.launchAuction(buyers);
		
		assertEquals(objectAuction.winner.buyerName, "A");
		assertEquals(objectAuction.winner.price, reservedPrice);
	}
	
	
	@Test
	public void examExampleTest() throws InterruptedException{
		ObjectToSell object = new ObjectToSell(reservedPrice);
		Auction objectAuction = new Auction(object);

		List<Buyer> buyers = new ArrayList<>();
		List<Integer> bidA = new LinkedList<>();
		List<Integer> bidB = new LinkedList<>();
		List<Integer> bidC = new LinkedList<>();
		List<Integer> bidD = new LinkedList<>();
		List<Integer> bidE = new LinkedList<>();
		bidA.add(110);
		bidA.add(130);
		bidB.add(0);
		bidC.add(125);
		bidD.add(105);
		bidD.add(115);
		bidD.add(90);
		bidE.add(132);
		bidE.add(135);
		bidE.add(140);
		Buyer a = new Buyer("A", bidA, objectAuction);
		Buyer b = new Buyer("B", bidB, objectAuction);
		Buyer c = new Buyer("C", bidC, objectAuction);
		Buyer d = new Buyer("D", bidD, objectAuction);
		Buyer e = new Buyer("E", bidE, objectAuction);
		buyers.add(a);
		buyers.add(b);
		buyers.add(c);
		buyers.add(d);
		buyers.add(e);

		objectAuction.launchAuction(buyers);
		
		assertEquals(objectAuction.winner.buyerName, "E");
		assertEquals(objectAuction.winner.price, 130);
	}
	
	@Test
	public void nonDeterministicTest() throws InterruptedException{
		ObjectToSell object = new ObjectToSell(reservedPrice);
		Auction objectAuction = new Auction(object);

		List<Buyer> buyers = new ArrayList<>();
		List<Integer> bidA = new LinkedList<>();
		List<Integer> bidB = new LinkedList<>();
		bidA.add(130);
		bidB.add(130);	
		Buyer a = new Buyer("A", bidA, objectAuction);
		Buyer b = new Buyer("B", bidB, objectAuction);	
		buyers.add(a);
		buyers.add(b);

		objectAuction.launchAuction(buyers);
		
		assertEquals(objectAuction.winner.price, 130);
		assertEquals(objectAuction.winner.buyerName, "A");
	}
	
	
}
