# blockDRM
The 'block dermatologist.'

Python front end-for the HyperLedger Composer. 


# Installation:
```
source env/bin/activate
pip3 install -e .
```

# Usage:
Run the CLI application with:
```
blockdrm
```


# Components:
Insert Game, requires the following:
```
asset Game identified by gameName {
    o String gameName
    o String gameKey
    o String description
    // o String mainExchange
    // o Double quantity
    --> User owner
}
```

Create User, requires the following:
```
participant User identified by userId {
    o String userId
    o String firstName
    o String lastName
}
```

Transactions--including user buying a game, and user gifting a game. Some combination of:
```
event TradeNotification {
    --> Game game
}

/*
event AddGameKey {
 	--> Game game 
}
*/

transaction RemoveHighQuantityGames {
}

event RemoveNotification {
    --> Game game
}
```




s





slide ideas:
```
"What constitues a JSON file?"
"First, I'd like to establish some key terms..."
```
