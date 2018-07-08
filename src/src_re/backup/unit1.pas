unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, FileUtil, Forms, Controls, Graphics, Dialogs, StdCtrls,RegExpr;

type

  { TForm1 }

  TForm1 = class(TForm)
    Button1: TButton;
    Memo1: TMemo;
    Memo2: TMemo;
    procedure Button1Click(Sender: TObject);
  private

  public

  end;

var
  Form1: TForm1;
  i:integer;
  re: TRegExpr;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.Button1Click(Sender: TObject);
begin
  re:=TRegExpr.Create('[А-Яăӑӗĕӳÿҫç]{1,100}/\*[А-Яăӑӗĕӳÿҫç]{1,100}((\$\^[.,:;!?()]/[.,:;!?()])<sent>)?\$');
  for i:=0 to Memo1.Lines.Count-1 do
  begin
    if re.Exec(Memo1.Lines.Strings[i]) then
      Memo2.Lines.Add(Memo1.Lines.Strings[i]);
  end;
end;

end.

