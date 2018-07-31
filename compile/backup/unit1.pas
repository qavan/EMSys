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
    Memo3: TMemo;
    procedure Button1Click(Sender: TObject);
  private

  public

  end;

var
  Form1: TForm1;
  i:integer;
  r:TRegExpr;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.Button1Click(Sender: TObject);
begin
  r:=TRegExpr.Create('\/\*');
  for i:=0 to Memo1.Lines.Count-1 do
  begin
     if r.Exec(Memo1.Lines.Strings[i]) then begin end else Memo3.Lines.Add(Memo2.Lines.Strings[i]);
  end;
end;

end.

