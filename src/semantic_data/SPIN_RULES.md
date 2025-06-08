# DriverStanding
```
PREFIX pred: <http://pitstop.org/pred/>
PREFIX ps: <http://pitstop.org/>

INSERT {
    ?s a ps:DriverStanding .
}
    WHERE {
    ?s a ps:Standing .
    ?s pred:hasDriver ?c .
}
```

# ConstructorStanding
```
PREFIX pred: <http://pitstop.org/pred/>
PREFIX ps: <http://pitstop.org/>

INSERT {
    ?s a ps:ConstructorStanding .
}
    WHERE {
    ?s a ps:Standing .
    ?s pred:hasConstructor ?c .
}
```

# Seasons
```
PREFIX pred: <http://pitstop.org/pred/>
PREFIX ps: <http://pitstop.org/>

INSERT {
    ?entity a ps:Season .
}
WHERE {
    ?entity pred:url ?url .
    FILTER NOT EXISTS {
        ?entity rdf:type ?anyType .
    }
}
```

