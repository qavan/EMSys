unit Unit3;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, FileUtil, Forms, Controls, Graphics, Dialogs, StdCtrls,RegExpr;

type

  { TForm3 }

  TForm3 = class(TForm)
    Button1: TButton;
    CheckBox1: TCheckBox;
    ComboBox1: TComboBox;
    Edit1: TEdit;
    Memo1: TMemo;
    Memo2: TMemo;
    procedure FormClose(Sender: TObject; var CloseAction: TCloseAction);
    procedure FormShow(Sender: TObject);
  private

  public

  end;

var
  Form3: TForm3;
  s:string;
  i:integer;
  j:integer;

implementation
uses unit1;

{$R *.lfm}

{ TForm3 }

procedure TForm3.FormShow(Sender: TObject);
begin
  Memo1.Clear;Memo2.Clear;Edit1.Clear;CheckBox1.Checked:=False;ComboBox1.ItemIndex:=0;
end;

procedure TForm3.FormClose(Sender: TObject; var CloseAction: TCloseAction);
begin
  //Form1.Visible:=True;
end;

end.

