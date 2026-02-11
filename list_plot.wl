(* ListPlotSimple: simple wrapper around ListPlot with sensible defaults *)
ListPlotSimple::usage = "ListPlotSimple[data_List, opts] plots a list of values with sensible defaults.";

Options[ListPlotSimple] = {
  PlotStyle -> Blue,
  Joined -> False,
  PlotMarkers -> Automatic,
  PlotRange -> All,
  AxesLabel -> {"Index", "Value"},
  ImageSize -> Medium
};

ListPlotSimple[data_List, opts : OptionsPattern[]] := Module[{optsApplied},
  optsApplied = FilterRules[{opts}, Options[ListPlotSimple]];
  ListPlot[Transpose[{Range[Length[data]], data}],
    Sequence @@ Normal[optsApplied]
  ]
];

(* Example:
   data = RandomReal[{0,1},20];
   ListPlotSimple[data, Joined->True, PlotStyle->Red]
*)
