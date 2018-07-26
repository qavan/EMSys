unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, FileUtil, Forms, Controls, Graphics, Dialogs, StdCtrls,RegExpr;

type

  { TForm1 }

  TForm1 = class(TForm)
    Button1: TButton;
    Button2: TButton;
    Edit1: TEdit;
    Memo1: TMemo;
    Memo2: TMemo;
    Memo3: TMemo;
    Memo4: TMemo;
    Memo5: TMemo;
    Memo6: TMemo;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
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
  re:=TRegExpr.Create(Edit1.Text);//[^0-9]\/\*[^0-9]
  for i:=0 to Memo1.Lines.Count-1 do
  begin
    if re.Exec(Memo2.Lines.Strings[i]) then
      begin
        Memo6.Lines.Add(Memo3.Lines.Strings[i]);
      end
    else
    begin
      Memo4.Lines.Add(Memo1.Lines.Strings[i]);
      Memo5.Lines.Add(Memo3.Lines.Strings[i]);
    end;
  end;
end;

procedure TForm1.Button2Click(Sender: TObject);
begin
  Memo1.Clear;Memo2.Clear;Memo3.Clear;Memo4.Clear;Memo5.Clear;Memo6.Clear;
end;

end.

