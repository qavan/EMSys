unit Unit4;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, FileUtil, Forms, Controls, Graphics, Dialogs, StdCtrls,RegExpr;

type

  { TForm4 }

  TForm4 = class(TForm)
    Button1: TButton;
    Edit1: TEdit;
    Edit2: TEdit;
    Edit3: TEdit;
    Memo1: TMemo;
    Memo2: TMemo;
    procedure Button1Click(Sender: TObject);
  private

  public

  end;

var
  Form4: TForm4;
  var i:integer;

implementation

{$R *.lfm}

{ TForm4 }

procedure TForm4.Button1Click(Sender: TObject);
var re: TRegExpr;
begin
  re:=TRegExpr.Create(Edit1.Text);
  Memo2.Lines.Add(Edit2.Text+'  to  '+Edit3.Text);
  for i:=1 to Memo1.Lines.Count do
   begin
    if re.Exec(Memo1.Lines.Strings[i]) then
      Memo1.Lines.Strings[i]:=Memo1.Lines.Strings[i].Replace(Edit2.Caption,Edit3.Caption);
   end;
end;

end.

