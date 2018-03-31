plot_trace = [
    {
        "type": "scatterpolargl",
        "r": dance,
        "theta": artist,
        "mode": "markers",
        "name": "Danceability",
        "marker": {
            "color": "rgb(27,158,119)",
            "size": 15,
            "line": {
                "color": "white"
            },
            "opacity": 0.7
        },
        "cliponaxis": 'false'
    },
    {
        "type": "scatterpolargl",
        "r": acoustic,
        "theta": artist,
        "mode": "markers",
        "name": "Acoustic",
        "marker": {
            "color": "rgb(217,95,2)",
            "size": 15,
            "line": {
                "color": "white"
            },
            "opacity": 0.7
        },
        "cliponaxis":"false"
    },
    {
        "type": "scatterpolargl",
        "r": valence,
        "theta": artist,
        "mode": "markers",
        "name": "Valence",
        "marker": {
            "color": "rgb(117,112,179)",
            "size": 15,
            "line": {
                "color": "white"
            },
            "opacity": 0.7
        },
        "cliponaxis": "false"
    },
    {
        "type": "scatterpolargl",
        "r": energy,
        "theta": artist,
        "mode": "markers",
        "name": "Energy",
        "marker": {
            "color": "rgb(231,41,138)",
            "size": 15,
            "line": {
                "color": "white"
            },
            "opacity": 0.7
        },
        "cliponaxis": "false"
    },
    {
        "type": "scatterpolargl",
        "r": bpm,
        "theta": artist,
        "mode": "markers",
        "name": "BPM",
        "marker": {
            "color": "rgb(102,166,30)",
            "size": 15,
            "line": {
                "color": "white"
            },
            "opacity": 0.7
        },
        "cliponaxis": "false"
    },
    {
        "type": "scatterpolargl",
        "r": loudness,
        "theta": artist,
        "mode": "markers",
        "name": "Loud",
        "marker": {
            "color": "rgb(230,171,2)",
            "size": 15,
            "line": {
                "color": "white"
            },
            "opacity": 0.7
        },
        "cliponaxis": "false"
    }
]