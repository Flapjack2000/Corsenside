using System.Collections.Generic;

class Program
{
	// Royal Flush, Straight Flush, Four of a Kind, Full House, Flush, Straight, Three of a Kind, Two Pair, Pair, High Card
	static void Main()
	{
		while (true)
		{
			Run();

			// Wait for input to keep going
			Console.ReadLine();
		}
	}
	static void Run()
	{
		// Set timer
		DateTime start = DateTime.Now;

		// Create deck and hand
		Deck d = new Deck();
		Hand hand = new Hand(d);

		PrintBorder();

		// Display cards and evaluate
		hand.DisplayHand();
		Console.WriteLine("Poker Hand: " + hand.EvaluateHand());

		// Show elapsed time
		Console.WriteLine("Time elapsed: " + (DateTime.Now - start).TotalMilliseconds + "ms");

		PrintBorder();
	}

	static void PrintBorder()
	{
		Console.WriteLine("------------------------------");
	}

	class Card
	{
		private readonly string suit;
		private readonly string rank;
		private readonly string name;
		private readonly int value;
		public Card(string rankName, string suitName)
		{
			suit = suitName;
			rank = rankName;

			if (!Deck.suits.Contains(suit.ToString()))
			{
				throw new Exception("Invalid card suit.");
			}

			// Assign card value based on rank, King=13, ..., Ten=10, ..., Ace=1
			value = rank switch
			{
				"King" => 13,
				"Queen" => 12,
				"Jack" => 11,
				"Ten" => 10,
				"Nine" => 9,
				"Eight" => 8,
				"Seven" => 7,
				"Six" => 6,
				"Five" => 5,
				"Four" => 4,
				"Three" => 3,
				"Two" => 2,
				"Ace" => 1,
				_ => throw new Exception("Invalid card value."),
			};

			// Create name of card from suit and rank
			name = rank + " of " + suit;
		}
		public string GetName()
		{
			return name;
		}
		public string GetSuit()
		{
			return suit;
		}
		public string GetRank()
		{
			return rank;
		}
		public int GetValue()
		{
			return value;
		}
	}

	class Deck : List<Card>
	{
		public static string[] suits = ["Hearts", "Diamonds", "Spades", "Clubs"];
		public static string[] ranks = ["King", "Queen", "Jack", "Ten", "Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "Ace"];

		public Deck()
		{
			// Generate deck of 52 cards
			foreach (string suit in suits)
			{
				foreach (string rank in ranks)
				{
					Add(new Card(rank, suit));
				}
			}
		}

		public void DisplayDeck()
		{
			// Print out indexed list of cards
			for (int i = 0; i < Count; i++)
			{
				Console.Write((i + 1).ToString() + " | ");
				Console.WriteLine(this[i].GetName());
			}
		}

		public void ShuffleDeck()
		{
			// Fisher-Yates shuffle
			int index = Count;
			Random rng = new Random();
			while (index > 1)
			{
				index--;
				int randomIndex = rng.Next(Count);
				(this[index], this[randomIndex]) = (this[randomIndex], this[index]);
			}
		}

		public List<Card> DrawFiveRandomCards()
		{
			ShuffleDeck();
			return GetRange(0, 5);
		}
	}

	class Hand : List<Card>
	{
		private readonly Dictionary<string, int> rankLookup = [];
		private List<int> pairCounter = [];

		public Hand(Deck deck)
		{
			List<Card> cards = deck.DrawFiveRandomCards().ToList();
			AddRange(cards);
		}

		public string EvaluateHand()
		{
			// Returns the highest ranking poker hand that can be made from the 5 cards in the hand.

			// Count the occurrences of each rank in the hand
			List<string> ranks = [.. from card in this select card.GetRank()];
			foreach (string rank in ranks)
			{
				if (rankLookup.ContainsKey(rank))
				{ rankLookup[rank]++; }
				else
				{ rankLookup[rank] = 1; }
			}

			// Count the number of pairs in the hand
			pairCounter = [.. from count in rankLookup.Values where count == 2 select count];

			if (CheckRoyalFlush())
			{
				return "Royal Flush";
			}
			else if (CheckStraightFlush())
			{
				return "Straight Flush";
			}
			else if (CheckFourOfAKind())
			{
				return "Four of a Kind";
			}
			else if (CheckFullHouse())
			{
				return "Full House";
			}
			else if (CheckFlush())
			{
				return "Flush";
			}
			else if (CheckStraight())
			{
				return "Straight";
			}
			else if (CheckThreeOfAKind())
			{
				return "Three of a Kind";
			}
			else if (CheckTwoPair())
			{
				return "Two Pair";
			}
			else if (CheckPair())
			{
				return "Pair";
			}
			else
			{
				return "High Card";
			}
		}

		public void DisplayHand()
		{
			// Print names of cards in hand
			for (int i = 0; i < Count; i++)
			{
				Console.Write((i + 1) + " | ");
				Console.WriteLine(this[i].GetName());
			}
		}

		public bool CheckRoyalFlush() 
		{
			List<string> royalValues = ["Ace", "King", "Queen", "Jack", "Ten"];
			List<string> foundValues = [.. from Card card in this select card.GetRank()];

			if (CheckFlush() && royalValues.All(rank => foundValues.Contains(rank)))
			{
				return true;
			}
			return false;
		}
		public bool CheckStraightFlush()
		{
			if (CheckFlush() && CheckStraight())
			{
				return true;
			}
			return false;
		}
		public bool CheckFourOfAKind()
		{
			// Four of a kind and one other card
			if (rankLookup.Values.Max() == 4 && rankLookup.Values.Min() == 1)
			{
				return true;
			}
			return false;
		}
		public bool CheckFullHouse()
		{
			if (rankLookup.Values.Max() == 3 && rankLookup.Values.Min() == 2)
			{
				return true;
			}
			return false;
		}
		public bool CheckFlush()
		{
			string suit = this[0].GetSuit();
			for (int i = 1; i < Count; i++)
			{
				if (this[i].GetSuit() != suit)
				{
					return false;
				}
			}
			return true;
		}
		public bool CheckStraight()
		{
			bool regularWay = true;
			bool otherWay = true;

			// Aces on bottom
			Sort((b, a) => a.GetValue().CompareTo(b.GetValue()));

			// Aces on top
			List<int> acesOnTop = [.. from card in this select card.GetValue()];
			for (int i = 0; i < acesOnTop.Count; i++)
			{
				if (acesOnTop[i] == 1)
				{
					// 14s beat Kings
					acesOnTop[i] = 14;
				}
			}

			// Sort in descending order
			acesOnTop.Sort();
			acesOnTop.Reverse();

			for (int i = 1; i < Count; i++)
			{
				if ((this[i].GetValue()) != (this[i - 1].GetValue() - 1))
				{
					regularWay = false;
				}

				if ((acesOnTop[i]) != (acesOnTop[i - 1] - 1))
				{
					otherWay = false;
				}
			}
			return regularWay || otherWay;
		}
		public bool CheckThreeOfAKind()
		{
			// Three of a kind and two other cards
			if (rankLookup.Values.Max() == 3 && rankLookup.Values.Min() == 1)
			{
				return true; 
			}
			return false;
		}
		public bool CheckTwoPair()
		{
			if ((rankLookup.Values.Max() == 2) && pairCounter.Count == 2)
			{
				return true;
			}
			return false;
		}
		public bool CheckPair()
		{
			if ((rankLookup.Values.Max() == 2) && pairCounter.Count == 1)
			{
				return true;
			}
			return false;
		}
	}
}