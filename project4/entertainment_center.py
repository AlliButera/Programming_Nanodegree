###############################################################################
# this file is where the instances of the Media (parent class) will be stored #
###############################################################################

# in order to run this file, referencing fresh_tomatoes and media (parent class)
import media
import fresh_tomatoes

# below are instances or children of the parent media class. Below are a few
# of my favorite instances or specific movies of media class.
# harry potter and the sorcerer's stone, the proposal, death at a funeral,
# london has fallen, the town, and the notebook

harry_potter_and_the_sorcerers_stone = media.Video("Harry Potter and the Sorcerer's Stone",
	"2 Hours 32 Minutes",
	"PG",
	"A muggle boy finds out he is a wizard by seeking adventure",
	"Adventure / Family / Fantasy",
	"Chris Columbus",
	"https://www.imdb.com/title/tt0241527/mediaviewer/rm683213568",
	"https://www.youtube.com/watch?v=PbdM1db3JbY")

the_proposal = media.Video("The Proposal",
	"1 Hour 48 Minutes",
	"PG-13",
	"A pushy boss foreces her assistant to marry her in order to keep her via status in the United States",
	"Comedy / Drama / Romance",
	"Anne Fletcher",
	"https://www.imdb.com/title/tt1041829/mediaviewer/rm2709856000",
	"https://www.youtube.com/watch?v=cVAEPPQfJ8I")

death_at_a_funeral = media.Video("Death At a Funeral",
	"1 Hour 32 Minutes",
	"A funeral ceremony turns into a debacle of exposed family secrets and misplaced bodies",
	"Comedy",
	"Dean Craig",
	"https://www.imdb.com/title/tt1321509/mediaviewer/rm3267133952",
	"https://www.youtube.com/watch?v=LkbR3nQqcrk")

london_has_fallen = media.Video("London Has Fallen",
	"1 Hour 39 Minutes",
	"R",
	"In London for the prime minister's funeral, mike banning is caught in a plot to assissinate all attending world leaders",
	"Action / Drama / Thriller",
	"Babak Najafi",
	"https://www.imdb.com/title/tt3300542/mediaviewer/rm2285037312",
	"https://www.youtube.com/watch?v=V45SkKt4Vhk")

the_town = media.Video("The Town",
	"2 Hours 5 Minutes",
	"R",
	"A longtime thief tries to balance his feelings for a bank manager connected to one of his earlier heists, as well as the F.B.I.",
	"Crime / Drama / Thriller",
	"Ben Affleck",
	"https://www.imdb.com/title/tt0840361/mediaviewer/rm1596030976",
	"https://www.youtube.com/watch?v=WcXt9aUMbBk")

the_notebook = media.Video("The Notebook",
	"2 HOurs 3 Minutes",
	"PG-13",
	"A poor, passionate man falls in love with a rich young woman giving him a sense of freedom",
	"Drama / Romance",
	"Nick Cassavetes",
	"https://www.imdb.com/title/tt0332280/mediaviewer/rm1153669376",
	"https://www.youtube.com/watch?v=FC6biTjEyZw")

# making a list of all instances or specific films reference above and assigning 
# it to a films variable.

films = [harry_potter_and_the_sorcerers_stone,the_proposal,death_at_a_funeral,
london_has_fallen,the_town,the_notebook]

# need to view website in browser, must point to fresh_tomatoes which contains
# html files

fresh_tomatoes.open_films_page(films)
