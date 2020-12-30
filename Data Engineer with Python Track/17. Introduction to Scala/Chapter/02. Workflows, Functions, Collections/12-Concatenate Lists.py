'''
Concatenate Lists


The triple-colon operator (:::) concatenates lists to create a new, combined list.

In Twenty-One, there are two major organizations that host competitive tournaments: the National Twenty-One Assocation (NTOA) and EuroTO, based in North America and Europe, respectively. Each league has a list of venues where they host their tournaments, venuesNTOA and venuesEuroTO. Recently, there was a merger of the organizations that made Twenty-One an overseas endeavor. NTOA and EuroTO were combined to create Twenty-One World. That means the list of venues must be combined, as tournaments will be played in both continents now.

In this exercise, you'll use the concatenation operator (:::) to create a new, combined venue list for Twenty-One World.

Instructions
100 XP

- Create the venuesNTOA list using List().
- Create the venuesEuroTO list using the cons operator (::).
- Concatenate venuesNTOA and venuesEuroTO to create a new list named venuesTOWorld.

'''
// The original NTOA and EuroTO venue lists
val venuesNTOA = List("The Grand Ballroom", "Atlantis Casino", "Doug's House")
val venuesEuroTO = "Five Seasons Hotel": : "The Electric Unicorn" : : Nil

// Concatenate the North American and European venues

val venuesTOWorld = venuesNTOA: : : venuesEuroTO
