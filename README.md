# Trade Network

> This Business Network illustrates commodity trading.

This business network defines:

**Participant**
`User`

**Asset**
`Game`

**Transaction(s)**
`Transaction`

**Event**
`TradeNotification `

To test this Business Network Definition in the **Test** tab:

Create two `User` participants:

```
{
  "$class": "org.acme.trading.User",
  "userId": "DEV1",
  "firstName": "Psyonix",
  "lastName": "Inc"
}
```

```
{
  "$class": "org.acme.trading.User",
  "userId": "USER1",
  "firstName": "Amy",
  "lastName": "Williams"
}
```

Create a `Game` asset:

```
{
  "$class": "org.acme.trading.Game",
  "gameName": "RL",
  "gameKey": "",
  "description": "Rocket League",
  "owner": "resource:org.acme.trading.User#DEV1"
}
```

Submit a `Trade` transaction:

```
{
  "$class": "org.acme.trading.Trade",
  "game": "resource:org.acme.trading.Game#RL",
  "newOwner": "resource:org.acme.trading.User#USER1"
}
```

After submitting this transaction, you should now see the transaction in the transaction registry. As a result, the owner of the game `RL` should now be owned `USER1` in the Asset Registry.

Congratulations!
